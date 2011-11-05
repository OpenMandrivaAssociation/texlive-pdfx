# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pdfx
# catalog-date 2009-05-04 11:07:03 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-pdfx
Version:	1.3
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package helps LaTeX users to create PDF/X-1a and PFD/A-1b
compliant pdf documents with pdfTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
