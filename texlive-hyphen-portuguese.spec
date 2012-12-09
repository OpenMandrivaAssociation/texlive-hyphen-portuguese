# revision 25990
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-portuguese
Version:	20120611
Release:	1
Summary:	Portuguese hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-portuguese.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Portuguese in T1/EC and UTF-8
encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-portuguese
%_texmf_language_def_d/hyphen-portuguese
%_texmf_language_lua_d/hyphen-portuguese

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-portuguese <<EOF
\%% from hyphen-portuguese:
portuguese loadhyph-pt.tex
=portuges
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-portuguese
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-portuguese <<EOF
\%% from hyphen-portuguese:
\addlanguage{portuguese}{loadhyph-pt.tex}{}{2}{3}
\addlanguage{portuges}{loadhyph-pt.tex}{}{2}{3}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-portuguese
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-portuguese <<EOF
-- from hyphen-portuguese:
	['portuguese'] = {
		loader = 'loadhyph-pt.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = { 'portuges' },
		patterns = 'hyph-pt.pat.txt',
		hyphenation = 'hyph-pt.hyp.txt',
	},
EOF


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120611-1
+ Revision: 804806
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120327-1
+ Revision: 787628
- Update to latest release.

* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120124-1
+ Revision: 767572
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 759932
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718674
- texlive-hyphen-portuguese
- texlive-hyphen-portuguese
- texlive-hyphen-portuguese
- texlive-hyphen-portuguese

