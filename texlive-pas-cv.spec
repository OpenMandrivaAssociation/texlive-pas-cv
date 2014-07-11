# revision 32263
# category Package
# catalog-ctan /macros/latex/contrib/pas-cv
# catalog-date 2013-11-27 22:13:58 +0100
# catalog-license lppl
# catalog-version 2.01
Name:		texlive-pas-cv
Version:	2.01
Release:	7
Summary:	Flexible typesetting of Curricula Vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pas-cv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-cv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-cv.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the framework for typesetting a Curriculum
Vitae (composed in French), together with a number of "themes"
that may be used with the package. (The use of the themes may
be seen in the package's examples/ collection.) The author
hints that conversion for use with other languages (than
French) should be possible.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pas-cv/macro-andromede.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-architecte.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-centaure.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-dynamique.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-gaia.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-jupiter.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-mars.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-neptune.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-orion.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-pegase.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-pluton.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-saturne.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-univers.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-uranus.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-venus.tex
%{_texmfdistdir}/tex/latex/pas-cv/pas-cv.sty
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-andromede.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-andromede.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-architecte.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-architecte.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-centaure.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-centaure.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-dynamique.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-dynamique.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-gaia.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-gaia.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-jupiter.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-jupiter.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-mars.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-mars.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-neptune.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-neptune.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-orion.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-orion.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-pegase.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-pegase.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-pluton.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-pluton.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-saturne.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-saturne.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-univers.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-univers.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-uranus.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-uranus.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-venus.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/examples/cv-venus.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/pas-cv.pdf
%doc %{_texmfdistdir}/doc/latex/pas-cv/pas-cv.tex
%doc %{_texmfdistdir}/doc/latex/pas-cv/photo.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
