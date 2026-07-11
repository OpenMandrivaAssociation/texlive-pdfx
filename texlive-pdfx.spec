%global tl_name pdfx
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6.5f
Release:	%{tl_revision}.1
Summary:	PDF/X and PDF/A support for pdfTeX, LuaTeX and XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package helps LaTeX users to create PDF/X, PFD/A and other
standards-compliant PDF documents with pdfTeX, LuaTeX and XeTeX.

