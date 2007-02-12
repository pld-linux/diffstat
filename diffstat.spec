Summary:	Provides diff file statistics
Summary(de.UTF-8):   Liefert diff-Datei-Statistiken
Summary(fr.UTF-8):   Fournit des statistiques sur les différences de fichiers
Summary(pl.UTF-8):   Umożliwia robienie statystyk plików diff
Summary(tr.UTF-8):   diff dosyası istatistik bilgileri çıkarır
Name:		diffstat
Version:	1.41
Release:	1
License:	distributable
Group:		Applications/Text
Source0:	ftp://invisible-island.net/diffstat/%{name}.tar.gz
# Source0-md5:	c4a55fea8f94dbd1664f76c98da4ee17
URL:		http://invisible-island.net/diffstat/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'diffstat' provides a number of statistics on a patch generated by
diff, including number of additions, number of removals, and total
number of changes. It can be useful, for example, to find out what
changes have been made to a program, just by feeding the update patch
to diffstat.

%description -l de.UTF-8
'diffstat' stellt eine Reihe von statistischen Informationen für mit
Patch erzeugte Diffs bereit, u.a. die Zahl der Einfügungen, der
Streichungen sowie die Gesamtzahl der Änderungen. So ist es möglich,
die Änderungen an einem Programm zu ermitteln, indem man das
Update-Patch durch diffstat durchlaufen läßt.

%description -l fr.UTF-8
« diffstat » offre de nombreuses statistiques sur un patch généré par
diff, cela comprend le nombre d'ajouts, de suppressions et le nombre
total de modifications. Il peut être utile, par exemple, de retrouver
les modifications faites à un programme en fournissant uniquement le
patch de mise à jour à diffstat.

%description -l pl.UTF-8
Diffstat umożliwia prowadzenie statystyk pliku (łatki) generowanego
przez diff. Pakiet ten może być użyteczny, na przykład w poszukiwaniu
zmian, które zostały dokonane w jakimś programie.

%description -l tr.UTF-8
diffstat programı, diff tarafından üretilen bir yama üzerinden toplama
sayısı, çıkarma sayısı, toplam değişiklik sayısı gibi bazı
istatistiksel bilgiler çıkartır.

%prep
%setup -q

%build
chmod -R u+w *
%{__autoconf}
%configure
%{__make} \
	CPPFLAGS="%{rpmcflags} -w" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install diffstat $RPM_BUILD_ROOT%{_bindir}
install diffstat.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
