Name:		texlive-pdfx
Version:	50338
Release:	2
Summary:	PDF/X-1a and PDF/A-1b support for pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package helps LaTeX users to create PDF/X-1a and PFD/A-1b
compliant pdf documents with pdfTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfx
%doc %{_texmfdistdir}/doc/latex/pdfx
#- source
%doc %{_texmfdistdir}/source/latex/pdfx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
