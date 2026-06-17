"""
=============================================================================
SISTEM PENDATAAN MAHASISWA
Aplikasi Desktop CRUD menggunakan Python 3 & Tkinter
Tugas Akhir - Pemrograman Berbasis Objek
=============================================================================
Author  : Sistem Pendataan Mahasiswa App
Teknologi: Python 3, Tkinter (built-in)
Database: In-memory (List of Dictionaries)
=============================================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox
import re


# =============================================================================
# CLASS UTAMA: SistemMahasiswa
# Mengelola seluruh logika aplikasi dan antarmuka pengguna
# =============================================================================
class SistemMahasiswa:
    """
    Kelas utama yang mengimplementasikan aplikasi CRUD Sistem Pendataan Mahasiswa.
    Menggunakan Tkinter untuk GUI dan list of dict sebagai penyimpanan data sementara.
    """

    def __init__(self, root):
        """
        Constructor: Inisialisasi window utama dan komponen aplikasi.
        Parameter:
            root (tk.Tk): Instance window Tkinter utama
        """
        self.root = root
        self.root.title("📚 Sistem Pendataan Mahasiswa")
        self.root.geometry("1050x680")
        self.root.resizable(True, True)
        self.root.minsize(900, 600)

        # ── Warna & Tema ──────────────────────────────────────────────────────
        self.COLOR_PRIMARY   = "#1565C0"   # Biru tua (header, tombol utama)
        self.COLOR_SECONDARY = "#1976D2"   # Biru sedang
        self.COLOR_ACCENT    = "#42A5F5"   # Biru muda
        self.COLOR_SUCCESS   = "#2E7D32"   # Hijau (Simpan)
        self.COLOR_WARNING   = "#E65100"   # Oranye (Edit)
        self.COLOR_DANGER    = "#C62828"   # Merah (Hapus)
        self.COLOR_NEUTRAL   = "#546E7A"   # Abu-abu biru (Reset)
        self.COLOR_SEARCH    = "#6A1B9A"   # Ungu (Cari)
        self.COLOR_BG        = "#F0F4F8"   # Latar belakang utama
        self.COLOR_CARD      = "#FFFFFF"   # Latar form/card
        self.COLOR_HEADER_FG = "#FFFFFF"   # Teks header
        self.COLOR_TEXT      = "#212121"   # Teks utama
        self.COLOR_SUBTEXT   = "#546E7A"   # Teks sekunder
        self.COLOR_ROW_ODD   = "#EEF2FF"   # Baris ganjil tabel
        self.COLOR_ROW_EVEN  = "#FFFFFF"   # Baris genap tabel

        # ── Penyimpanan Data (in-memory) ──────────────────────────────────────
        # Setiap mahasiswa disimpan sebagai dictionary
        self.data_mahasiswa = []
        self.selected_index = None       # Index baris yang dipilih di tabel

        # ── Variabel StringVar untuk field form ───────────────────────────────
        self.var_nim    = tk.StringVar()
        self.var_nama   = tk.StringVar()
        self.var_prodi  = tk.StringVar()
        self.var_smt    = tk.StringVar()
        self.var_telp   = tk.StringVar()
        self.var_search = tk.StringVar()

        # ── Build UI ──────────────────────────────────────────────────────────
        self.root.configure(bg=self.COLOR_BG)
        self._build_header()
        self._build_main_content()
        self._build_status_bar()

        # ── Data Awal (contoh dummy) ──────────────────────────────────────────
        self._load_sample_data()
        self._refresh_table()

    # =========================================================================
    # BUILD UI: Header
    # =========================================================================
    def _build_header(self):
        """Membuat bagian header aplikasi dengan judul dan deskripsi."""
        header_frame = tk.Frame(self.root, bg=self.COLOR_PRIMARY, pady=14)
        header_frame.pack(fill="x")

        tk.Label(
            header_frame,
            text="📚  SISTEM PENDATAAN MAHASISWA",
            font=("Segoe UI", 18, "bold"),
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_HEADER_FG
        ).pack()

        tk.Label(
            header_frame,
            text="Aplikasi CRUD Desktop | Python 3 + Tkinter",
            font=("Segoe UI", 9),
            bg=self.COLOR_PRIMARY,
            fg="#BBDEFB"
        ).pack()

    # =========================================================================
    # BUILD UI: Konten Utama (Form + Tabel)
    # =========================================================================
    def _build_main_content(self):
        """Membangun area konten utama yang memuat form input dan tabel data."""
        main = tk.Frame(self.root, bg=self.COLOR_BG)
        main.pack(fill="both", expand=True, padx=14, pady=10)

        # Kolom kiri: Form input
        self._build_form_panel(main)

        # Kolom kanan: Tabel + Search
        self._build_table_panel(main)

    # ─── Panel Kiri: Form Input ───────────────────────────────────────────────
    def _build_form_panel(self, parent):
        """
        Membangun panel form input di sisi kiri.
        Berisi field NIM, Nama, Prodi, Semester, No Telepon, dan tombol aksi.
        """
        left = tk.Frame(parent, bg=self.COLOR_BG, width=310)
        left.pack(side="left", fill="y", padx=(0, 10))
        left.pack_propagate(False)

        # ── Card Form ────────────────────────────────────────────────────────
        card = tk.Frame(left, bg=self.COLOR_CARD, relief="flat",
                        highlightbackground="#CBD5E1", highlightthickness=1)
        card.pack(fill="x", pady=(0, 10))

        # Judul form
        tk.Frame(card, bg=self.COLOR_PRIMARY, height=4).pack(fill="x")
        tk.Label(
            card, text="  Form Data Mahasiswa",
            font=("Segoe UI", 11, "bold"),
            bg=self.COLOR_CARD, fg=self.COLOR_PRIMARY,
            anchor="w", pady=8
        ).pack(fill="x", padx=14)

        # ── Fields ──────────────────────────────────────────────────────────
        form_body = tk.Frame(card, bg=self.COLOR_CARD, padx=14, pady=6)
        form_body.pack(fill="x")

        fields = [
            ("NIM *",              self.var_nim,   "Contoh: 2024001"),
            ("Nama Mahasiswa *",   self.var_nama,  "Nama lengkap"),
            ("Program Studi *",    self.var_prodi, "Contoh: Teknik Informatika"),
            ("Semester *",         self.var_smt,   "1 s/d 14"),
            ("Nomor Telepon *",    self.var_telp,  "Contoh: 08123456789"),
        ]

        self.entry_refs = {}
        for label_text, var, placeholder in fields:
            # Label
            tk.Label(
                form_body, text=label_text,
                font=("Segoe UI", 9, "bold"),
                bg=self.COLOR_CARD, fg=self.COLOR_TEXT,
                anchor="w"
            ).pack(fill="x", pady=(6, 1))

            # Entry
            entry = ttk.Entry(form_body, textvariable=var, font=("Segoe UI", 10))
            entry.pack(fill="x", ipady=5)

            # Placeholder hint (label kecil)
            tk.Label(
                form_body, text=placeholder,
                font=("Segoe UI", 7),
                bg=self.COLOR_CARD, fg="#9E9E9E",
                anchor="w"
            ).pack(fill="x")

            self.entry_refs[label_text] = entry

        # Spasi bawah form
        tk.Frame(card, bg=self.COLOR_CARD, height=10).pack()

        # ── Tombol Aksi ──────────────────────────────────────────────────────
        btn_card = tk.Frame(left, bg=self.COLOR_CARD, relief="flat",
                            highlightbackground="#CBD5E1", highlightthickness=1)
        btn_card.pack(fill="x")
        tk.Frame(btn_card, bg=self.COLOR_PRIMARY, height=4).pack(fill="x")
        tk.Label(
            btn_card, text="  Aksi",
            font=("Segoe UI", 11, "bold"),
            bg=self.COLOR_CARD, fg=self.COLOR_PRIMARY,
            anchor="w", pady=8
        ).pack(fill="x", padx=14)

        btn_frame = tk.Frame(btn_card, bg=self.COLOR_CARD, padx=14, pady=8)
        btn_frame.pack(fill="x")

        # Definisi tombol: (teks, warna, perintah, deskripsi hover)
        buttons = [
            ("💾  Simpan",  self.COLOR_SUCCESS,  self.create_mahasiswa, "Tambah data baru"),
            ("✏️  Edit",    self.COLOR_WARNING,  self.update_mahasiswa, "Perbarui data terpilih"),
            ("🗑️  Hapus",   self.COLOR_DANGER,   self.delete_mahasiswa, "Hapus data terpilih"),
            ("🔄  Reset",   self.COLOR_NEUTRAL,  self.reset_form,       "Bersihkan form"),
        ]

        for (text, color, cmd, _) in buttons:
            tk.Button(
                btn_frame,
                text=text,
                font=("Segoe UI", 10, "bold"),
                bg=color,
                fg="white",
                relief="flat",
                cursor="hand2",
                pady=8,
                command=cmd,
                activebackground=color,
                activeforeground="white",
                bd=0,
                highlightthickness=0
            ).pack(fill="x", pady=3)

        # Info total mahasiswa
        tk.Frame(btn_card, bg=self.COLOR_CARD, height=4).pack()
        self.lbl_total = tk.Label(
            btn_card,
            text="Total: 0 mahasiswa",
            font=("Segoe UI", 9),
            bg=self.COLOR_CARD,
            fg=self.COLOR_SUBTEXT,
            pady=6
        )
        self.lbl_total.pack()

    # ─── Panel Kanan: Tabel + Search ──────────────────────────────────────────
    def _build_table_panel(self, parent):
        """
        Membangun panel tabel di sisi kanan.
        Berisi form pencarian dan Treeview untuk menampilkan data.
        """
        right = tk.Frame(parent, bg=self.COLOR_BG)
        right.pack(side="left", fill="both", expand=True)

        # ── Card Pencarian ───────────────────────────────────────────────────
        search_card = tk.Frame(right, bg=self.COLOR_CARD, relief="flat",
                               highlightbackground="#CBD5E1", highlightthickness=1)
        search_card.pack(fill="x", pady=(0, 8))

        tk.Frame(search_card, bg=self.COLOR_SEARCH, height=4).pack(fill="x")

        search_inner = tk.Frame(search_card, bg=self.COLOR_CARD, padx=14, pady=8)
        search_inner.pack(fill="x")

        tk.Label(
            search_inner, text="🔍  Cari Mahasiswa:",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_CARD, fg=self.COLOR_SEARCH
        ).pack(side="left")

        self.entry_search = ttk.Entry(
            search_inner, textvariable=self.var_search,
            font=("Segoe UI", 10), width=28
        )
        self.entry_search.pack(side="left", padx=8, ipady=5)

        tk.Button(
            search_inner,
            text="Cari",
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_SEARCH, fg="white",
            relief="flat", cursor="hand2",
            padx=12, pady=4,
            command=self.search_mahasiswa,
            activebackground=self.COLOR_SEARCH,
            activeforeground="white"
        ).pack(side="left", padx=(0, 6))

        tk.Button(
            search_inner,
            text="Tampilkan Semua",
            font=("Segoe UI", 9),
            bg=self.COLOR_NEUTRAL, fg="white",
            relief="flat", cursor="hand2",
            padx=12, pady=4,
            command=self.show_all,
            activebackground=self.COLOR_NEUTRAL,
            activeforeground="white"
        ).pack(side="left")

        # Bind Enter key pada field search
        self.entry_search.bind("<Return>", lambda e: self.search_mahasiswa())

        # ── Card Tabel ───────────────────────────────────────────────────────
        table_card = tk.Frame(right, bg=self.COLOR_CARD, relief="flat",
                              highlightbackground="#CBD5E1", highlightthickness=1)
        table_card.pack(fill="both", expand=True)

        tk.Frame(table_card, bg=self.COLOR_SECONDARY, height=4).pack(fill="x")

        tk.Label(
            table_card, text="  Data Mahasiswa",
            font=("Segoe UI", 11, "bold"),
            bg=self.COLOR_CARD, fg=self.COLOR_SECONDARY,
            anchor="w", pady=8
        ).pack(fill="x", padx=14)

        # Frame untuk Treeview + scrollbar
        tree_frame = tk.Frame(table_card, bg=self.COLOR_CARD)
        tree_frame.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        # Scrollbar vertikal
        scrollbar_y = ttk.Scrollbar(tree_frame, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")

        # Scrollbar horizontal
        scrollbar_x = ttk.Scrollbar(tree_frame, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        # ── Treeview ─────────────────────────────────────────────────────────
        cols = ("No", "NIM", "Nama", "Program Studi", "Semester", "No. Telepon")
        self.tree = ttk.Treeview(
            tree_frame,
            columns=cols,
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
            selectmode="browse",
            height=18
        )
        self.tree.pack(fill="both", expand=True)
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)

        # Konfigurasi kolom header dan lebar
        col_configs = {
            "No":            (40,  "center"),
            "NIM":           (100, "center"),
            "Nama":          (200, "w"),
            "Program Studi": (180, "w"),
            "Semester":      (70,  "center"),
            "No. Telepon":   (120, "center"),
        }

        for col in cols:
            w, anchor = col_configs[col]
            self.tree.heading(col, text=col, anchor="center",
                              command=lambda c=col: self._sort_column(c))
            self.tree.column(col, width=w, anchor=anchor, minwidth=40)

        # Style Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        rowheight=28,
                        font=("Segoe UI", 9),
                        background=self.COLOR_CARD,
                        fieldbackground=self.COLOR_CARD,
                        foreground=self.COLOR_TEXT)
        style.configure("Treeview.Heading",
                        font=("Segoe UI", 9, "bold"),
                        background=self.COLOR_SECONDARY,
                        foreground="white",
                        relief="flat")
        style.map("Treeview",
                  background=[("selected", self.COLOR_ACCENT)],
                  foreground=[("selected", "white")])

        # Tag warna baris bergantian
        self.tree.tag_configure("odd",  background=self.COLOR_ROW_ODD)
        self.tree.tag_configure("even", background=self.COLOR_ROW_EVEN)

        # Event klik baris
        self.tree.bind("<<TreeviewSelect>>", self._on_row_select)
        self.tree.bind("<Double-1>", self._on_double_click)

    # ─── Status Bar ──────────────────────────────────────────────────────────
    def _build_status_bar(self):
        """Membangun status bar di bagian bawah jendela aplikasi."""
        status_frame = tk.Frame(self.root, bg=self.COLOR_PRIMARY, pady=4)
        status_frame.pack(fill="x", side="bottom")

        self.lbl_status = tk.Label(
            status_frame,
            text="✅ Aplikasi siap digunakan.",
            font=("Segoe UI", 8),
            bg=self.COLOR_PRIMARY,
            fg="#BBDEFB",
            anchor="w",
            padx=14
        )
        self.lbl_status.pack(side="left")

        tk.Label(
            status_frame,
            text="Python 3 + Tkinter  |  Data disimpan sementara",
            font=("Segoe UI", 8),
            bg=self.COLOR_PRIMARY,
            fg="#BBDEFB",
            anchor="e",
            padx=14
        ).pack(side="right")

    # =========================================================================
    # DATA AWAL: Sample Data
    # =========================================================================
    def _load_sample_data(self):
        """Memuat data mahasiswa contoh untuk demonstrasi awal."""
        samples = [
            {"nim": "2024001", "nama": "Andi Pratama",       "prodi": "Teknik Informatika",   "semester": "4", "telp": "081234567890"},
            {"nim": "2024002", "nama": "Budi Santoso",       "prodi": "Sistem Informasi",      "semester": "2", "telp": "085678901234"},
            {"nim": "2024003", "nama": "Citra Dewi",         "prodi": "Teknik Elektro",        "semester": "6", "telp": "087890123456"},
            {"nim": "2023010", "nama": "Dian Kurniawan",     "prodi": "Manajemen Informatika", "semester": "5", "telp": "089012345678"},
            {"nim": "2023011", "nama": "Eka Putri Rahayu",   "prodi": "Teknik Informatika",   "semester": "3", "telp": "082345678901"},
        ]
        for s in samples:
            self.data_mahasiswa.append(s)

    # =========================================================================
    # CRUD: CREATE — Tambah data mahasiswa baru
    # =========================================================================
    def create_mahasiswa(self):
        """
        CREATE: Menambahkan data mahasiswa baru ke dalam list penyimpanan.
        Melakukan validasi field kosong dan duplikasi NIM sebelum menyimpan.
        """
        # Ambil nilai dari form
        nim    = self.var_nim.get().strip()
        nama   = self.var_nama.get().strip()
        prodi  = self.var_prodi.get().strip()
        smt    = self.var_smt.get().strip()
        telp   = self.var_telp.get().strip()

        # ── Validasi field tidak boleh kosong ──────────────────────────────
        if not all([nim, nama, prodi, smt, telp]):
            messagebox.showwarning(
                "⚠️ Peringatan",
                "Semua field wajib diisi!\nPastikan tidak ada field yang kosong."
            )
            return

        # ── Validasi format NIM (angka saja, min 5 digit) ──────────────────
        if not nim.isdigit() or len(nim) < 5:
            messagebox.showwarning(
                "⚠️ Format NIM",
                "NIM harus berupa angka dan minimal 5 digit.\nContoh: 2024001"
            )
            return

        # ── Validasi Semester (angka 1-14) ─────────────────────────────────
        if not smt.isdigit() or not (1 <= int(smt) <= 14):
            messagebox.showwarning(
                "⚠️ Format Semester",
                "Semester harus berupa angka antara 1 hingga 14."
            )
            return

        # ── Validasi Nomor Telepon (angka, diawali 08, min 10 digit) ───────
        if not re.match(r"^08\d{8,11}$", telp):
            messagebox.showwarning(
                "⚠️ Format Telepon",
                "Nomor telepon tidak valid.\nHarus diawali '08' dan terdiri dari 10-13 digit.\nContoh: 08123456789"
            )
            return

        # ── Cek duplikasi NIM ──────────────────────────────────────────────
        for mhs in self.data_mahasiswa:
            if mhs["nim"] == nim:
                messagebox.showerror(
                    "❌ NIM Duplikat",
                    f"NIM '{nim}' sudah terdaftar!\nGunakan NIM yang berbeda."
                )
                return

        # ── Simpan data baru ───────────────────────────────────────────────
        mahasiswa_baru = {
            "nim":      nim,
            "nama":     nama,
            "prodi":    prodi,
            "semester": smt,
            "telp":     telp
        }
        self.data_mahasiswa.append(mahasiswa_baru)
        self._refresh_table()
        self.reset_form()
        self._set_status(f"✅ Data mahasiswa '{nama}' (NIM: {nim}) berhasil ditambahkan.")
        messagebox.showinfo(
            "✅ Berhasil",
            f"Data mahasiswa '{nama}' berhasil ditambahkan!"
        )

    # =========================================================================
    # CRUD: READ — Tampilkan data di tabel
    # =========================================================================
    def _refresh_table(self, data=None):
        """
        READ: Memperbarui tampilan Treeview dengan data terkini.
        Parameter:
            data (list|None): Data yang akan ditampilkan; jika None, tampilkan semua.
        """
        # Bersihkan isi tabel
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Gunakan semua data jika tidak ada filter
        tampil = data if data is not None else self.data_mahasiswa

        # Isi tabel dengan data
        for i, mhs in enumerate(tampil, start=1):
            tag = "odd" if i % 2 != 0 else "even"
            self.tree.insert("", "end", values=(
                i,
                mhs["nim"],
                mhs["nama"],
                mhs["prodi"],
                mhs["semester"],
                mhs["telp"]
            ), tags=(tag,))

        # Perbarui label total
        total = len(tampil)
        self.lbl_total.config(text=f"Total: {total} mahasiswa")

    # =========================================================================
    # CRUD: UPDATE — Edit data mahasiswa terpilih
    # =========================================================================
    def update_mahasiswa(self):
        """
        UPDATE: Memperbarui data mahasiswa yang dipilih dari tabel.
        Mengambil nilai form dan mengganti data pada index yang sesuai.
        """
        # Pastikan ada baris yang dipilih
        if self.selected_index is None:
            messagebox.showwarning(
                "⚠️ Pilih Data",
                "Silakan pilih data mahasiswa yang ingin diedit terlebih dahulu."
            )
            return

        # Ambil nilai baru dari form
        nim    = self.var_nim.get().strip()
        nama   = self.var_nama.get().strip()
        prodi  = self.var_prodi.get().strip()
        smt    = self.var_smt.get().strip()
        telp   = self.var_telp.get().strip()

        # ── Validasi field kosong ──────────────────────────────────────────
        if not all([nim, nama, prodi, smt, telp]):
            messagebox.showwarning(
                "⚠️ Peringatan",
                "Semua field wajib diisi sebelum menyimpan perubahan!"
            )
            return

        # ── Validasi format ────────────────────────────────────────────────
        if not nim.isdigit() or len(nim) < 5:
            messagebox.showwarning("⚠️ Format NIM", "NIM harus berupa angka minimal 5 digit.")
            return
        if not smt.isdigit() or not (1 <= int(smt) <= 14):
            messagebox.showwarning("⚠️ Format Semester", "Semester harus angka antara 1-14.")
            return
        if not re.match(r"^08\d{8,11}$", telp):
            messagebox.showwarning("⚠️ Format Telepon", "Nomor telepon tidak valid.\nContoh: 08123456789")
            return

        # ── Cek duplikasi NIM (boleh sama dengan NIM milik sendiri) ────────
        nim_lama = self.data_mahasiswa[self.selected_index]["nim"]
        for i, mhs in enumerate(self.data_mahasiswa):
            if mhs["nim"] == nim and i != self.selected_index:
                messagebox.showerror("❌ NIM Duplikat", f"NIM '{nim}' sudah digunakan mahasiswa lain!")
                return

        # ── Konfirmasi update ──────────────────────────────────────────────
        konfirmasi = messagebox.askyesno(
            "🔄 Konfirmasi Edit",
            f"Apakah Anda yakin ingin mengubah data mahasiswa ini?\n\nNIM: {nim}\nNama: {nama}"
        )
        if not konfirmasi:
            return

        # ── Simpan perubahan ───────────────────────────────────────────────
        self.data_mahasiswa[self.selected_index] = {
            "nim":      nim,
            "nama":     nama,
            "prodi":    prodi,
            "semester": smt,
            "telp":     telp
        }
        self._refresh_table()
        self.reset_form()
        self._set_status(f"✅ Data mahasiswa '{nama}' (NIM: {nim}) berhasil diperbarui.")
        messagebox.showinfo("✅ Berhasil", f"Data mahasiswa '{nama}' berhasil diperbarui!")

    # =========================================================================
    # CRUD: DELETE — Hapus data mahasiswa terpilih
    # =========================================================================
    def delete_mahasiswa(self):
        """
        DELETE: Menghapus data mahasiswa yang dipilih dari tabel setelah konfirmasi.
        """
        # Pastikan ada baris yang dipilih
        if self.selected_index is None:
            messagebox.showwarning(
                "⚠️ Pilih Data",
                "Silakan pilih data mahasiswa yang ingin dihapus terlebih dahulu."
            )
            return

        # Nama mahasiswa untuk pesan konfirmasi
        mhs = self.data_mahasiswa[self.selected_index]
        nama_hapus = mhs["nama"]
        nim_hapus  = mhs["nim"]

        # Konfirmasi penghapusan
        konfirmasi = messagebox.askyesno(
            "🗑️ Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus data berikut?\n\n"
            f"NIM  : {nim_hapus}\nNama : {nama_hapus}\n\n"
            f"⚠️ Data yang dihapus tidak dapat dikembalikan!"
        )
        if not konfirmasi:
            return

        # Hapus dari list
        del self.data_mahasiswa[self.selected_index]
        self._refresh_table()
        self.reset_form()
        self._set_status(f"🗑️ Data mahasiswa '{nama_hapus}' (NIM: {nim_hapus}) berhasil dihapus.")
        messagebox.showinfo("✅ Berhasil", f"Data mahasiswa '{nama_hapus}' berhasil dihapus!")

    # =========================================================================
    # SEARCH: Cari mahasiswa berdasarkan NIM atau Nama
    # =========================================================================
    def search_mahasiswa(self):
        """
        SEARCH: Mencari mahasiswa berdasarkan NIM atau Nama (case-insensitive).
        Menampilkan hasil filter di tabel tanpa menghapus data asli.
        """
        keyword = self.var_search.get().strip().lower()

        if not keyword:
            messagebox.showwarning(
                "⚠️ Pencarian Kosong",
                "Masukkan kata kunci pencarian (NIM atau Nama)!"
            )
            return

        # Filter data berdasarkan NIM atau Nama
        hasil = [
            mhs for mhs in self.data_mahasiswa
            if keyword in mhs["nim"].lower() or keyword in mhs["nama"].lower()
        ]

        if hasil:
            self._refresh_table(hasil)
            total = len(hasil)
            self._set_status(f"🔍 Ditemukan {total} mahasiswa dengan kata kunci '{keyword}'.")
        else:
            # Tabel dikosongkan, tampilkan pesan
            self._refresh_table([])
            self._set_status(f"🔍 Tidak ditemukan mahasiswa dengan kata kunci '{keyword}'.")
            messagebox.showinfo(
                "🔍 Hasil Pencarian",
                f"Tidak ditemukan data mahasiswa dengan kata kunci:\n'{keyword}'"
            )

    # =========================================================================
    # SHOW ALL: Tampilkan semua data (reset filter pencarian)
    # =========================================================================
    def show_all(self):
        """Menampilkan seluruh data mahasiswa (menghapus filter pencarian aktif)."""
        self.var_search.set("")
        self._refresh_table()
        self._set_status("✅ Menampilkan semua data mahasiswa.")

    # =========================================================================
    # RESET FORM
    # =========================================================================
    def reset_form(self):
        """Mengosongkan semua field pada form input dan mereset pilihan."""
        self.var_nim.set("")
        self.var_nama.set("")
        self.var_prodi.set("")
        self.var_smt.set("")
        self.var_telp.set("")
        self.selected_index = None
        # Deselect baris di tabel
        for item in self.tree.selection():
            self.tree.selection_remove(item)
        self._set_status("🔄 Form direset. Siap untuk input data baru.")

    # =========================================================================
    # EVENT: Klik baris di tabel
    # =========================================================================
    def _on_row_select(self, event):
        """
        Event handler saat pengguna memilih baris pada Treeview.
        Mengisi form dengan data baris yang dipilih.
        """
        selected = self.tree.selection()
        if not selected:
            return

        # Ambil nilai dari baris yang dipilih
        values = self.tree.item(selected[0], "values")
        if not values:
            return

        # values = (No, NIM, Nama, Prodi, Semester, Telp)
        nim_terpilih = values[1]

        # Cari index di data_mahasiswa berdasarkan NIM
        for i, mhs in enumerate(self.data_mahasiswa):
            if mhs["nim"] == nim_terpilih:
                self.selected_index = i
                break

        # Isi form dengan data terpilih
        self.var_nim.set(values[1])
        self.var_nama.set(values[2])
        self.var_prodi.set(values[3])
        self.var_smt.set(values[4])
        self.var_telp.set(values[5])

        self._set_status(f"📌 Dipilih: {values[2]} (NIM: {values[1]})")

    def _on_double_click(self, event):
        """Event handler untuk double-click pada baris tabel (isi form + info)."""
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            messagebox.showinfo(
                "ℹ️ Detail Mahasiswa",
                f"NIM          : {values[1]}\n"
                f"Nama         : {values[2]}\n"
                f"Program Studi: {values[3]}\n"
                f"Semester     : {values[4]}\n"
                f"No. Telepon  : {values[5]}"
            )

    # =========================================================================
    # SORT: Klik header kolom untuk mengurutkan
    # =========================================================================
    def _sort_column(self, col):
        """
        Mengurutkan data tabel berdasarkan kolom yang diklik.
        Parameter:
            col (str): Nama kolom yang diklik
        """
        col_map = {
            "No":            None,
            "NIM":           "nim",
            "Nama":          "nama",
            "Program Studi": "prodi",
            "Semester":      "semester",
            "No. Telepon":   "telp",
        }
        key = col_map.get(col)
        if not key:
            return

        # Toggle arah sorting
        if not hasattr(self, "_sort_reverse"):
            self._sort_reverse = {}
        self._sort_reverse[col] = not self._sort_reverse.get(col, False)

        if key == "semester":
            self.data_mahasiswa.sort(key=lambda x: int(x[key]) if x[key].isdigit() else 0,
                                     reverse=self._sort_reverse[col])
        else:
            self.data_mahasiswa.sort(key=lambda x: x[key].lower(),
                                     reverse=self._sort_reverse[col])

        self._refresh_table()
        arah = "↓" if self._sort_reverse[col] else "↑"
        self._set_status(f"🔀 Diurutkan berdasarkan '{col}' {arah}")

    # =========================================================================
    # UTILITAS: Update status bar
    # =========================================================================
    def _set_status(self, pesan):
        """
        Memperbarui teks pada status bar.
        Parameter:
            pesan (str): Pesan yang ditampilkan di status bar
        """
        self.lbl_status.config(text=pesan)


# =============================================================================
# ENTRY POINT
# =============================================================================
def main():
    """Fungsi utama untuk menjalankan aplikasi."""
    root = tk.Tk()
    app  = SistemMahasiswa(root)
    root.mainloop()


if __name__ == "__main__":
    main()