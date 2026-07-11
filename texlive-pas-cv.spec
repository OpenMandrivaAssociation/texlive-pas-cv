%global tl_name pas-cv
%global tl_revision 32263

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.01
Release:	%{tl_revision}.1
Summary:	Flexible typesetting of Curricula Vitae
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pas-cv
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-cv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-cv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the framework for typesetting a Curriculum Vitae
(composed in French), together with a number of "themes" that may be
used with the package. (The use of the themes may be seen in the
package's examples/ collection.) The author hints that conversion for
use with other languages (than French) should be possible.

