%global tl_name hyphen-portuguese
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Portuguese hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-portuguese
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-portuguese.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Portuguese in T1/EC and UTF-8 encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-portuguese:
portuguese loadhyph-pt.tex
=portuges
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-portuguese:
\addlanguage{portuguese}{loadhyph-pt.tex}{}{2}{3}
\addlanguage{portuges}{loadhyph-pt.tex}{}{2}{3}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-portuguese:
['portuguese'] = {
	loader = 'loadhyph-pt.tex',
	lefthyphenmin = 2,
	righthyphenmin = 3,
	synonyms = { 'portuges' },
	patterns = 'hyph-pt.pat.txt',
	hyphenation = 'hyph-pt.hyp.txt',
},
TL_HYPHEN_EOF
