Name:		texlive-sectionbreak
Version:	50339
Release:	1
Summary:	LaTeX support for section breaks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sectionbreak
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sectionbreak.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sectionbreak.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX support for section breaks, used
mainly in fiction books to signal changes in a story, like
changes in time, location, etc. It supports the asterism
symbol, text content, or custom macros as the section break
mark symbol.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/sectionbreak
%doc %{_texmfdistdir}/doc/latex/sectionbreak

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
