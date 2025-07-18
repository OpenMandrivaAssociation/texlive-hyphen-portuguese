Name:		texlive-hyphen-portuguese
Version:	74203
Release:	1
Summary:	Portuguese hyphenation patterns
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-portuguese.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-portuguese
%_texmf_language_def_d/hyphen-portuguese
%_texmf_language_lua_d/hyphen-portuguese

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-portuguese <<EOF
\%% from hyphen-portuguese:
portuguese loadhyph-pt.tex
=portuges
=brazil
=brazilian
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-portuguese
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-portuguese <<EOF
\%% from hyphen-portuguese:
\addlanguage{portuguese}{loadhyph-pt.tex}{}{2}{3}
\addlanguage{portuges}{loadhyph-pt.tex}{}{2}{3}
\addlanguage{brazil}{loadhyph-pt.tex}{}{2}{3}
\addlanguage{brazilian}{loadhyph-pt.tex}{}{2}{3}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-portuguese
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-portuguese <<EOF
-- from hyphen-portuguese:
	['portuguese'] = {
		loader = 'loadhyph-pt.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = { 'portuges', 'brazil', 'brazilian' },
		patterns = 'hyph-pt.pat.txt',
		hyphenation = 'hyph-pt.hyp.txt',
	},
EOF
