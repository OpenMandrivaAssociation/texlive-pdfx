# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pdfx
# catalog-date 2009-05-04 11:07:03 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-pdfx
Version:	1.3
Release:	2
Summary:	PDF/X-1a and PDF/A-1b support for pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfx.source.tar.xz
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
%{_texmfdistdir}/tex/latex/pdfx/glyphtounicode-cmr.tex
%{_texmfdistdir}/tex/latex/pdfx/pdfa-1b.xmp
%{_texmfdistdir}/tex/latex/pdfx/pdfx-1a.xmp
%{_texmfdistdir}/tex/latex/pdfx/pdfx.sty
%doc %{_texmfdistdir}/doc/latex/pdfx/README
%doc %{_texmfdistdir}/doc/latex/pdfx/manifest.txt
%doc %{_texmfdistdir}/doc/latex/pdfx/pdfx.pdf
%doc %{_texmfdistdir}/doc/latex/pdfx/small2e.pdf
%doc %{_texmfdistdir}/doc/latex/pdfx/small2e.tex
%doc %{_texmfdistdir}/doc/latex/pdfx/small2e.xmpdata
#- source
%doc %{_texmfdistdir}/source/latex/pdfx/Makefile
%doc %{_texmfdistdir}/source/latex/pdfx/pdfx.dtx
%doc %{_texmfdistdir}/source/latex/pdfx/pdfx.ins
%doc %{_texmfdistdir}/source/latex/pdfx/rvdtx.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 754806
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 719231
- texlive-pdfx
- texlive-pdfx
- texlive-pdfx

