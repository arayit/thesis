%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%% OzU-Thesis.cls (v1.0)
%% Copyright (c) 2012 by M. Oguz Sunay. All rights reserved.
%% See licensing information, below.
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\ozuthesisversion}{1.0}% current version number
\newcommand{\ozuthesisupdated}{2012/06/19}% date of last change(s)
\usepackage{times}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  
%%  LaTeX2e class file for formatting documents according to the
%%  Graduate School of Sciences and Engineering guidelines for 
%%  theses at Ozyegin University 
%%  
%%  USAGE:  \documentclass{ozu-thesis}
%%          \documentclass[...options...]{ozu-thesis}
%%  
%%  The default settings produce a final copy, ready for submission
%%  (11pt font, single-sided, double-spaced, normal margins,
%%  with single-spaced notes).
%%  
%%  OPTIONS:
%%  
%%   - Any standard option for the LaTeX2e ``report'' class, including
%%     ``10pt'', ``11pt'', ``12pt'', ``oneside'', ``twoside'', etc.
%%  
%%   - ``singlespaced'', ``oneandahalfspaced'', or ``doublespaced'':  Set
%%     the entire document's default line spacing, except for notes,
%%     which are single-spaced by default.
%%  
%%   - ``spacednotes'':  Let the line spacing of notes be determined
%%     by the line spacing of the main document, instead of being
%%     forced single-spaced.
%%  
%%   - ``narrowmargins'', ``normalmargins'', ``widemargins'', 
%%     ``extrawidemargins'' or ``oldmargins'':  Set the size of 
%%     the margins, as follows:
%%      . ``normal'': 1 1/2" on left, 1" on top, right and bottom
%%        headers & footers 1/4" from body;
%%        - This is the OzU standard
%%      . ``narrow'': 1 1/4" on the left, 3/4" on all other sides,
%%        headers & footers 1/4" from body;
%%      . ``wide'': 1 1/4" on all sides, headers & footers 3/4" from
%%        body;
%%      . ``extrawide'': 1 1/2" on all sides, headers & footers 3/4"
%%        from body.
%%      . ``oldmargins'': 1 1/2" on left and top, 1" on right and bottom
%%        headers & footers 1/2 from body;
%%        adds 2"" extra space from top of page, on the first
%%        page of a chapter or appendix.
%%     (If you have more than just a few marginal notes, it is
%%     recommended that you use ``wide'' or ``extrawide'' margins.)
%%     Use ``normalmargins'' (the default) for the approved GT format.
%%
%%   - ``draft'':  Produce a draft copy (10pt font, double-sided,
%%     double-spaced, normal margins, with the word "DRAFT" printed
%%     at all four corners of every page, and current date printed in
%%     a running footer).
%%
%%   - ``hyperref'': Indicates that the document will \usepackage{hyperref}.
%%     This is a kludge, but I didn't want to explicitly *require*
%%     hyperref, so we must indicate to ozu-thesis.cls whether it should
%%     define certain hyperref commands as dummies.  ALWAYS use this
%%     option if you use the hyperref package.  NEVER use this option if
%%     you do not also use the hyperref package.
%%  
%%  Note that these options can be used to override the default or
%%  draft document settings, so that it is possible, for example,
%%  to create a double-sided final copy, or a 1 1/2-spaced draft
%%  copy with wide margins, etc.  Also note that when producing
%%  double-sided documents, new chapters and preliminary sections
%%  will always start on a right-hand page under the default
%%  settings (inserting a blank page if needed), but not if the
%%  ``draft'' option was used.  (This can be overriden by using the
%%  ``openany'' or ``openright'' options.  To achieve this effect for
%%  individual sections or chapters, use the \cleardoublepage
%%  command.)  Note that the blank page inserted in these cases will
%%  still contain the header and page number that is present on all
%%  pages.  For ``empty'' or ``plain'' pages, explicitly use one of the
%%  commands \clearemptydoublepage (totally blank inserted pages),
%%  \clearplaindoublepage (blank except for page number at bottom), or
%%  \cleartcplainfdoublepage (blank except for page number at Top
%%  Corner (hence, TCplain).  You can also explicitly use 
%%  \clearozuthesisdoublepage (but I don't know why you would, since this
%%  only makes sense if the current pagestyle is already ozuthesis, and
%%  if that is the case then you're better off just using \cleardoublepage.
%%  
%%   ENVIRONMENTS and COMMANDS:
%%   In some cases there will be two commands with identical
%%   effect.  
%%
%%   * \title{...}:  (preamble only; REQUIRED)
%%
%%   * \author{...}:  (preamble only; REQUIRED)
%%     Specify the name of the author.
%%
%%   * \department{...}:    (preamble only; REQUIRED)
%%   * \dept{...}:          compatibility synonym
%%     Specify the name of the graduate department.
%%
%%   * \major{...}:  (preamble only; REQUIRED if \listmajortrue is set)
%%
%%   * \degree{...}:  (preamble only; REQUIRED)
%%     Specify the name of the degree (e.g., "Doctor of Philosophy").
%%  
%%   * \gradyear{...}:      (preamble only; REQUIRED)
%%   * \copyrightyear{...}: compatibility synonym
%%     Specify the year of graduation (defaults to current year).
%%
%%   * \principaladvisor{...}:  (preamble only; OPTIONAL)
%%     (or \principaladviser{...}, if you prefer advisor spelled with an e)
%%
%%   * \committeechair{...}: (preamble only; OPTIONAL)
%%
%%   * \firstmember{...}:    (preamble only; OPTIONAL)
%%   * \secondmember{...}:   (preamble only; OPTIONAL)
%%   * \thirdmember{...}:    (preamble only; OPTIONAL)
%%   * \fourthmember{...}:   (preamble only; OPTIONAL)
%%   * \fifthmember{...}:    (preamble only; OPTIONAL)
%%   * \sixthmember{...}:    (preamble only; OPTIONAL)
%%
%%   * \submitdate{month year in which submitted}
%%     date is LaTeX'd if not specified
%%   * \approveddate{month, day, and year on which the last committee
%%      member signs the thesis form} (preamble only; REQUIRED)
%%
%%   * \titlepagetrue or \titlepagefalse
%%     - produce or don't produce a title page (TRUE by default)
%%
%%   * \signaturepagetrue or \signaturepagefalse
%%     - produce or don't produce a signature page (TRUE by default)
%%
%%   * \copyrighttrue or \copyrightfalse
%%     - place or don't place a copyright notice on the title page (FALSE by default)
%%
%%   * \figurespagetrue or \figurespagefalse
%%     - produce or don't produce a List of Figures page (TRUE by default)
%%
%%   * \tablespagetrue or \tablespagefalse
%%     - produce or don't produce a List of Tables page (TRUE by default)
%%
%%   * \contentspagetrue or \contentspagefalse
%%     - produce or don't produce a Table of Contents page (TRUE by default)
%%
%%   * \bibpagetrue or \bibpagefalse
%%     - produce or don't produce a Bibliography page (TRUE by default)
%%
%%   * \thesisproposaltrue or \thesisproposalfalse
%%     - indicate "Thesis Proposal" or "Thesis" on the title page (FALSE by default)
%%
%%   * \dedicationheadingtrue or \dedicationheadingfalse
%%     - display ``DEDICATION'' heading on the dedication page (FALSE by default)
%%
%%   * \dedicationtop and \dedicationbottom
%%     - The Graduate Office Guidelines say that the dedication should be centered
%%       on the page.  By default, this is done -- but IMO it looks ugly.  The
%%       vertical spacing above and below your text is proided by these two
%%       macros; redefined them if you want to do something different.  E.g.
%%       this looks nice:
 %%        \renewcommand{\dedicationtop}{\vspace*{\stretch{1}}
%%         \renewcommand{\dedicationbottom{\vspace*{\stretch{3}}
%%       which places the dedication about 1/4 of the way down the page.
%%
%%   * \strictmarginstrue or \strictmarginsfalse
%%     - if true, then obey the margin rules EVEN on the title and signature
%%       page. Default TRUE and REQUIRED by Graduate Studies Office, but
%%       not very appealing.  (under ``oldmargins'' an extra 50p spacing is
%%       added so that the title page looks like the chapter headings
%%       In any case, \strictmarginsfalse looks better for personal copies
%%       but \strictmarginstrue is necessary for official ones.
%%
%%   * \multivolumetrue or \multivolumefalse
%%     - if true, indicates that the thesis will span multiple volumes. 
%%       triggers automatic generation of the first volume title page
%%       (in addition to the ``entire work'' title page), but it's up
%%       to you to place the ``part{}'' commands in the appropriate
%%       locations for volume 2, volume 3, etc.
%% 
%%   * \listmajortrue or \listmajorfalse
%%     - If true, puts ``In Partial Fulfillment...[degree] in
%%       [major]'' on the title page and then puts the department down
%%       with \"{O}zye\u{g}in University at the bottom of the
%%       page. If false, puts ``In Partial Fulfillment...[degree] in
%%       the [department]'' on the title page.
%%
%%   * \dissertationtrue or \dissertationfalse
%%     - If true, uses the word ``Dissertation'' on the title page. If
%%       false, uses ``thesis''.
%%
%%   * \bibfiles{...}
%%    Set the list of bibfiles to use when generating a bibliography   
%%  
%%   - \linespacing{...}:  (preamble only)
%%   - \spacing{...}:      compatibility synonym
%%     Set the interline spacing directly, overriding document
%%     defaults and options; note that in order to get the correct
%%     appearance, the argument to \linespacing must be equal to
%%     1/3 + 2/3 times the desired line spacing (for example,
%%        single-spaced = \linespacing{1},
%%         1 1/2-spaced = \linespacing{1.25}, and
%%        double-spaced = \linespacing{1.66}).
%%
%%   - ignore{...}:
%%   - comment{...}:     compatibility synonym
%%     Ignore the part of the file between { and } (can include
%%     paragraph breaks); useful for commenting out large blocks.
%%  
%%   - \clearemptydoublepage, \clearplaindoublepage, 
%%     \cleartcplaindoublepage, \clearozuthesisdoublepage
%%     Same as \cleardoublepage except that it sets the pagestyle of
%%     any inserted blank page to ``empty'' ``plain'' ``tcplain'' or
%%     ``ozuthesis'' respectively.
%% 
%%   - \begin{preliminary}...\end{preliminary}:
%%     Delimit head matter (title page, abstract, table of contents,
%%     lists of tables and figures, etc.): set the page style and
%%     numbering for the preliminary sections and reset them for the
%%     main document.
%%    + Alternatively, at the appropriate spots call the synonymous 
%%      \beforepreface and \afterpreface.  These ``synonyms'' do
%%      the same setup tasks as \begin{preliminary} and \end{preliminary},
%%      but they don't create an ``environment.  The use of these
%%      synonyms is NOT recommended for new documents and are provided 
%%      only for backward compatibility.
%%
%%      - \beforepreface:
%%        Sets pagestyle and generates titlepage (via \maketitle)
%%        and signature page (via \makesignature) if indicated.
%%        DON'T call directly in new documents.  Use \begin{preliminary}
%%        instead.
%%
%%      - \afterpreface:
%%        Sets pagestyle back to normal, restarts page numbering
%%        DON'T call directly in new documents.  Use \end{preliminary}
%%        instead.
%%  
%%      - \maketitle:
%%        Generate the title page from the information supplied
%%        in the preamble.  Called automatically by \begin{preliminary}
%%        or \beforepreface.
%%
%%      - \makesignature:
%%        Generate a signature page from information supplied 
%%        in the preamble.  Called automatically by \begin{preliminary}
%%        or \beforepreface.
%%  
%%      - \begin{dedication}...\end{dedication}:
%%        Generate a dedication section, if needed.
%%  
%%      - \begin{acknowledgements}...\end{acknowledgements}:
%%        Generate an acknowledgements section, if needed.
%%
%%      - \begin{abstract}...\end{abstract}:
%%        Generate the abstract page.
%%  
%%
%%      - \contents
%%        Prints table of contents, list of figures, and list of
%%        tables as indicated by \contentspagetrue, \figurespagetrue,
%%        and \tablespagetrue
%%
%%      - Modifying the look of the Table of Contents:
%%
%%        + \labelchaptersintableofcontents 
%%          inserts an entry into the TOC that says ``CHAPTERS'' just 
%%          before Chapter 1.
%%
%%        + \labelappendicesintableofcontents
%%          inserts an entry into the TOC that says ``APPENDICES'' just 
%%          before Appendix A.
%%        
%%        + \settocstring
%%          change the name used for the Table of Contents (def: 'Table of Contents')
%%        
%%        + \setlofstring
%%          change the name used for the List of Figures (def: 'List of Figures')
%%
%%        + \setlotstring
%%          change the name used for the List of Tables (def: 'List of Tables')
%%
%%        + \setchaptertocdepth
%%          set the default for how ``deep'' to number within chapters
%%          in the table of contents.
%%
%%        + \setappendixtocdepth
%%          set the default for how ``deep'' to number within appendices
%%          (chapter{}'s after the \appendix command) in the table of
%%          contents
%%
%%        + \settocdepth
%%          temporarily change how "deep" to number in the table of 
%%          contents for current chapter/section.  For example, you
%%          usually include \section{}'s in the TOC (\setchaptertocdepth{1})
%%          but in chapter 5 you want to include subsection as well:
%%          \chapter{This is Chapter 5}\settocdepth{2}.  In cahapter 6 the
%%          default depth of 1 is reasserted.
%%  
%%         You should never need to call \setcounter{tocdepth}{..} directly.
%%         0 = chapter only
%%         1 = chapter + sections
%%         2 = chapter, section, subsection
%%         3 = chapter, section, subsection, subsubsection
%%
%%        Recommended structure for frontmatter:
%%     \begin{document}
%%       \begin{preliminary}
%%         \begin{dedication}...\end{dedication}
%%         \begin{abstract}...\end{abstract}
%%         \begin{ozetce}...\end{ozetce}
%%         \begin{acknowledgements}...\end{acknowledgements}
%%         \contents
%%       \end{preliminary}
%%
%%  
%%   - \begin{longquote}...\end{longquote}:
%%     Single-spaced version of the ``quote'' environment.
%%  
%%   - \begin{longquotation}...\end{longquotation}:
%%     Single-spaced version of the ``quotation'' environment.
%%  
%%   - \begin{singlespaced}...\end{singlespaced}:
%%     Format single-spaced paragraphs.
%%  
%%   - \begin{oneandahalfspaced}...\end{oneandahalfspaced}:
%%     Format 1 1/2-spaced paragraphs.
%%  
%%   - \begin{doublespaced}...\end{doublespaced}:
%%     Format double-spaced paragraphs.
%%  
%%   - \begin{newspacing}{<n>}...\end{newspacing}:
%%     Format paragraphs with an interline spacing of ``n''.
%%  
%%  (Note that the last four environments can be used to change the
%%  default line spacing of any enclosed text, including figures,
%%  tables, abstract or acknowledgement pages, table of contents,
%%  etc.)
%%
%%   - \appendix: a global mode switch (just like the report class).
%%     changes the way ``chapter'' headings and TOC entries are 
%%     generated.
%%       \chapter{last chapter titled}...
%%       \appendix
%%       \chapter{first appendix title}...
%%
%%   - \begin{postliminary}...\end{postliminary}:
%%     Delimit end matter (bibliography, vita, etc).
%%    + Alternatively, call the synonyms
%%      \beforepostface and \afterpostface instead.  These
%%      synonyms are provided for backward compatibility with
%%      ozuthesis.sty; their use is not recommended for new documents.
%%
%%
%%
%%      - \begin{vita}...\end{vita}:
%%        Generate a vita page 
%%
%%      - \references:
%%        Generate bibliography if indicated by bibliographytrue
%%        NOTE: you must set \bibpagetrue AND \bibfiles{file1,file2,...}
%%        in the preample, AND you must set \bibliographystyle{...} just
%%        after \begin{document}.  Otherwise \references won't work.
%%
%%      - \postfacesection{other-title}{...text...}
%%        Used to specify endsections that do not have
%%        custom environments defined for them above.
%%
%%
%%     Recommended structure for frontmatter:
%%     \begin{postliminary}
%%       \references 
%%       \begin{vita}...\end{vita}
%%     \end{postliminary} 
%%
%%  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%        IDENTIFICATION        %%%%%%%%%%%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ozu-thesis}
        [\ozuthesisupdated\space\ozuthesisversion\space(M. Oguz Sunay)]%
\RequirePackage{calc}% part of LaTeX tools bundle   
%\RequirePackage{lastpage}

\def\ozuthesis@checkVersion#1{\edef\reserved@a{#1}%
  \ifx \ozuthesis@version \reserved@a
    \expandafter\@gobble
  \else
    \expandafter\@firstofone
  \fi}
\xdef\ozuthesis@version{\ozuthesisversion}

%%%%%%%%%%%%         INITIAL CODE         %%%%%%%%%%%%

%% To comment out parts of a file.
%
\newcommand{\ignore}[1]{}
\newcommand{\comment}[1]{}

%% Switch for testing draft mode (toggled by ``draft'' option).
%
\newif\if@draft
\@draftfalse % initially false by default

%% Switch for testing current page style.
%
\newif\if@tcpage
 % no default value (set by \pagestyle)
 % indicates that page numbers are in the upper corners

%% Switch for testing line spacing of notes.
%
\newif\if@singlespacednotes
\@singlespacednotestrue % initially true by default

%% Switch for testing the hyperref option
%
\newif\if@hyperref
\@hyperreffalse % initially false by default

%% Macro for testing the size of margins.
%
\newcommand{\@marginsize}{}

%
\newcommand{\@thesisptsz}{}
\newcommand{\@thesisside}{}
\newcommand{\@thesisopen}{}
\newcommand{\@thesislnsp}{}


%%%%%%%%%%%%      OPTION DECLARATION      %%%%%%%%%%%%

%% ``draft'' option: change default document settings.
%
\DeclareOption{draft}{\@drafttrue
   \typeout{ozu-Thesis Class Option: ``draft''}
   \ExecuteOptions{10pt,twoside,openany,doublespaced,normalmargins}
   \PassOptionsToClass{draft}{report}
   %% Macros for printing "DRAFT" at the corners of a page.
   \newcommand{\tlDRAFT}%
     {\raisebox{ 3ex}[0pt][0pt]{\llap{\sffamily\scriptsize DRAFT\ \ }}}
   \newcommand{\trDRAFT}%
     {\raisebox{ 3ex}[0pt][0pt]{\rlap{\sffamily\scriptsize \ \ DRAFT}}}
   \newcommand{\blDRAFT}%
     {\raisebox{-3ex}[0pt][0pt]{\llap{\sffamily\scriptsize DRAFT\ \ }}}
   \newcommand{\brDRAFT}%
     {\raisebox{-3ex}[0pt][0pt]{\rlap{\sffamily\scriptsize \ \ DRAFT}}}
}%DeclareOption{draft}

%% ``spacednotes'' option: make notes share the line spacing of the rest
%% of the document.
%
\DeclareOption{spacednotes}{\@singlespacednotesfalse}

%% Margin options: change the size of margins.
%% choose normalmargins option for Georgia Tech thesis format
%
\DeclareOption{narrowmargins}{\renewcommand{\@marginsize}{0}}
\DeclareOption{normalmargins}{\renewcommand{\@marginsize}{1}}
\DeclareOption{widemargins}{\renewcommand{\@marginsize}{2}}
\DeclareOption{extrawidemargins}{\renewcommand{\@marginsize}{3}}
\DeclareOption{oldmargins}{\renewcommand{\@marginsize}{4}}

%% Point Size options: change current setting.
%
\DeclareOption{10pt}{\renewcommand{\@thesisptsz}{10pt}}
\DeclareOption{11pt}{\renewcommand{\@thesisptsz}{11pt}}
\DeclareOption{12pt}{\renewcommand{\@thesisptsz}{12pt}}

%% Number of Page Sides options: change current setting.
%
\DeclareOption{twoside}{\renewcommand{\@thesisside}{twoside}}
\DeclareOption{oneside}{\renewcommand{\@thesisside}{oneside}}

%% New Chapter Openings options: change current setting.
%
\DeclareOption{openany}{\renewcommand{\@thesisopen}{openany}}
\DeclareOption{openright}{\renewcommand{\@thesisopen}{openright}}

%% Line Spacing options: change current setting.
%
\DeclareOption{singlespaced}{\renewcommand{\@thesislnsp}{1}}
\DeclareOption{oneandahalfspaced}{\renewcommand{\@thesislnsp}{1.25}}
%\DeclareOption{doublespaced}{\renewcommand{\@thesislnsp}{1.66}}
\DeclareOption{doublespaced}{\renewcommand{\@thesislnsp}{1.66}}

%% STUPID HACK for hyperref, \@chapter, and \MakeUppercase
%
\newcommand{\Makeuppercase}[1]{\MakeUppercase{#1}}
\DeclareOption{hyperref}{%
  \@hyperreftrue
%  \renewcommand{\Makeuppercase}[1]{%
%    \ifHy@pdfstring#1\else\MakeUppercase{#1}\fi}
}

%% All other options are passed to the base class directly.
%
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}


%%%%%%%%%%%%       OPTION EXECUTION       %%%%%%%%%%%%

%% Default settings.
%
\ExecuteOptions{11pt,letterpaper,oneside,%
openright,doublespaced,normalmargins,final}
%
%% Process options.
%
\ProcessOptions


%%%%%%%%%%%%       PACKAGE  LOADING       %%%%%%%%%%%%

%% Load base class using current setting for basic options.
%
\LoadClass[\@thesisptsz,\@thesisside,\@thesisopen]{report}


%% From lastpage package. Used to generate abstract.
%% Lastpage is written by Jeff Goldberg (J.Goldberg@Cranfield.ac.uk)
%% It is relased under the GPL (version 2)

\def\lastpage@putlabel{\addtocounter{page}{-1}%
   \immediate\write\@auxout{\string
   \newlabel{LastPage}{{}{\thepage}{}{}{}}}%
   \addtocounter{page}{1}}


%%%%%%%%%%%%          MAIN  CODE          %%%%%%%%%%%%

\if@hyperref
\else
  \newcommand{\phantomsection}{}% helps with hyperref.  \phantomsection
%                                 is provided by pdflatex, but not latex.
  \newcommand{\texorpdfstring}[2]{#1}%
  \def\pdfbookmark[#1]#2#3{}%
\fi


%%%%%%    Line Spacing
%
%% \linespacing is used to define the default line spacing. 
%% for the entire document. If the argument is less than 
%% 1.25 (for 1.5-spaced) a warning message is displayed
%% when not in draft mode.
%%
%% Don't use this command for temporary, localized changes.
%% Instead, use the ``spacing environments'':
%%    \begin{singlespace}      ...\end{singlespaced}
%%    \begin{oneandahalfspaced}...\end{oneandahalfspaced}
%%    \begin{doublespaed}      ...\end{doublespaced}
%%    \begin{longquote}        ...\end{longquote}
%%    \begin{longquotation}    ...\end{longquotation}
%%    \begin{newspacing}{x.xx} ...\end{newspacing}
%
\newcommand{\linespacing}[1]{%
  \gdef\@spacing{#1}
  \newlinestretch{#1}\if@draft\else\ifdim #1pt < 1.25pt\typeout
   {ozu-Thesis Class Warning: line spacing less than 1 1/2}\fi\fi
}
%
%% \spacing is a clone of \linespacing, retained for backwards
%% compatibility with ozuthesis.sty
%
\newcommand{\spacing}[1]{%
  \gdef\@spacing{#1}
  \newlinestretch{#1}\if@draft\else\ifdim #1pt < 1.25pt\typeout
  {ozu-Thesis Class Warning: line spacing less than 1 1/2}\fi\fi
}
\def\@spacing{1.66}

%
%% ``longquote'' and ``longquotation'' produce single-spaced quotes, while
%% ``newspacing'' encloses paragraphs with a different line spacing,
%% such as ``singlespaced'', ``oneandahalfspaced'', or ``doublespaced''.
%
\newenvironment{longquote}%
  {\begin{quote}\newlinestretch{1}}{\end{quote}}
\newenvironment{longquotation}%
  {\begin{quotation}\newlinestretch{1}}{\end{quotation}}
\newenvironment{singlespaced}%
  {\begin{newspacing}{1}}{\end{newspacing}}
\newenvironment{oneandahalfspaced}%
  {\begin{newspacing}{1.25}}{\end{newspacing}}
\newenvironment{doublespaced}%
  {\begin{newspacing}{1.66}}{\end{newspacing}}
\newenvironment{newspacing}[1]%
  {\par\begingroup\newlinestretch{#1}}%
  {\par\vskip\parskip\vskip\baselineskip\endgroup
   \vskip-\parskip\vskip-\baselineskip}

%
%% To change the actual line spacing.
%
\newcommand{\newlinestretch}[1]%
  {\renewcommand{\baselinestretch}{#1}\currenttextsize}

%
%% To keep track of the current text size.
%
\let\currenttextsize=\normalsize
%
%% Redefine size-changing commands to update \currenttextsize.
%
\let\tmp@tiny=\tiny
\renewcommand{\tiny}%
  {\let\currenttextsize=\tmp@tiny\tmp@tiny}
\let\tmp@scriptsize=\scriptsize
\renewcommand{\scriptsize}%
  {\let\currenttextsize=\tmp@scriptsize\tmp@scriptsize}
\let\tmp@footnotesize=\footnotesize
\renewcommand{\footnotesize}%
  {\let\currenttextsize=\tmp@footnotesize\tmp@footnotesize}
\let\tmp@small=\small
\renewcommand{\small}%
  {\let\currenttextsize=\tmp@small\tmp@small}
\let\tmp@normalsize=\normalsize
\renewcommand{\normalsize}%
  {\let\currenttextsize=\tmp@normalsize\tmp@normalsize}
\let\tmp@large=\large
\renewcommand{\large}%
  {\let\currenttextsize=\tmp@large\tmp@large}
\let\tmp@Large=\Large
\renewcommand{\Large}%
  {\let\currenttextsize=\tmp@Large\tmp@Large}
\let\tmp@LARGE=\LARGE
\renewcommand{\LARGE}%
  {\let\currenttextsize=\tmp@LARGE\tmp@LARGE}
\let\tmp@huge=\huge
\renewcommand{\huge}%
  {\let\currenttextsize=\tmp@huge\tmp@huge}
\let\tmp@Huge=\Huge
\renewcommand{\Huge}%
  {\let\currenttextsize=\tmp@Huge\tmp@Huge}
%
%% Make notes single-spaced if ``spacednotes'' option was not given.
%% Note that this does _not_ change the spacing of figures or tables.
%
\if@singlespacednotes
%% Make footnotes single-spaced.
\let\tmp@@footnotetext=\@footnotetext
\renewcommand{\@footnotetext}[1]%
  {{\newlinestretch{1}\tmp@@footnotetext{#1}}}
%% Make footnotes inside a minipage single-spaced.
\let\tmp@@mpfootnotetext=\@mpfootnotetext
\renewcommand{\@mpfootnotetext}[1]%
  {{\newlinestretch{1}\tmp@@mpfootnotetext{#1}}}
%% Make marginal notes single-spaced.
\let\tmp@@marginparreset=\@marginparreset
\renewcommand{\@marginparreset}%
  {\newlinestretch{1}\tmp@@marginparreset}
\fi%@singlespacednotes
% 
%%%%%%    New formatting environments and commands.
%
%% \begin{preliminary} sets the pagestyle and pagenumbering 
%% (roman numeral format ) for the preliminary sections; 
%% It also calls \beforepreface to create the title page
%% and signature page if indicated by \titlepagetrue and/or
%% \signaturepageture.
%%
%% \end{preliminary} resets the pagenumbering. To start page 
%% numbering in arabic format, use \pagestyle{plain} and 
%% \pagenumbering{arabic} after the preliminary environment block
%
\newenvironment{preliminary}%
  {  
    \newlinestretch{1.0}%
    \pagenumbering{roman}%
    \pagestyle{\front@pagestyle}%
    \iftitlepage%
      \maketitle%
    \fi%
    \ifmultivolume%
      \part{}%
    \fi%
    \ifsignaturepage%
      \makesignature%
    \fi%
    \newlinestretch{\@spacing}%
  }%
  {%
    \if@draft%
    \else%
      \if@twoside%
        \if@openright%
          \cleardoublepage%
        \fi%
      \fi%
    \fi%
    \newpage%
    \pagenumbering{arabic}%
    \pagestyle{\body@pagestyle}%
    \newlinestretch{\@spacing}%
  }%

%%%%%%    Front Matter Parameters
%
%% The following commands set the respective field values so we
%% can generate the title page, signature page, and abstract
%% page automatically
%
\renewcommand{\author}[1]%
  {\ifx\empty#1\empty\else\gdef\@author{#1}\fi}
\newcommand{\mainadvisor}[1]%
  {\ifx\empty#1\empty\else\gdef\@mainadvisor{#1}\fi}
\newcommand{\coadvisor}[1]%
  {\ifx\empty#1\empty\else\gdef\@coadvisor{#1}\fi}
\renewcommand{\title}[1]%
  {\ifx\empty#1\empty\else\gdef\@title{#1}\fi}

\newcommand{\degree}[1]%
  {\ifx\empty#1\empty\else\gdef\@degree{#1}\fi}
%
%% Is this a thesis, or a thesis proposal ?
%
\newif\ifthesisproposal
\thesisproposalfalse % default to thesis, not thesis proposal

%
%% Is this a thesis or a dissertation?
%
\newif\ifdissertation
\dissertationfalse % default to thesis

%
%% Do we list the major in the ``Partial Fulfillment'' block or the department?
%
\newif\iflistmajor
\listmajorfalse % default to listing the department

\newif\ifcoadvisor
\coadvisorfalse

\newcommand{\major}[1]%
   {\ifx\empty#1\empty\else\gdef\@major{#1}\fi}

%
%% \department and \dept are synonymous
%
\newcommand{\department}[1]%
  {\ifx\empty#1\empty\else\gdef\@department{#1}\gdef\@dept{#1}\fi}
\newcommand{\dept}[1]%
  {\ifx\empty#1\empty\else\gdef\@department{#1}\gdef\@dept{#1}\fi}
\newcommand{\faculty}[1]%
  {\ifx\empty#1\empty\else\gdef\@faculty{#1}\fi}
%
%% date stuff
%% \gradyear and \copyrightyear are synonymmous
%
\newcommand{\gradyear}[1]%
  {\ifx\empty#1\empty\else\gdef\@gradyear{#1}\gdef\@copyrightyear{#1}\fi}
\newcommand{\copyrightyear}[1]%
  {\ifx\empty#1\empty\else\gdef\@gradyear{#1}\gdef\@copyrightyear{#1}\fi}
\newcommand{\submitdate}[1]%
  {\ifx\empty#1\empty\else\gdef\@submitdate{#1}\fi}
\newcommand{\approveddate}[1]%
  {\ifx\empty#1\empty\else\gdef\@approveddate{#1}\fi}
%
\def\advis@r{Advisor} % default spelling

% Define \principaladvisor{} to take two optional arguments after the
% name. Thus, the usage is 
%    \principaladvisor{Advisor Name}[Advisor Unit][Advisor Institution]
% Advisor Unit defaults to \@department and Advisor Institution
% defaults to \"{O}zye\u{g}in University.
\def\principaladvisor[#1]{#1}

\def\principaladvisor@i#1[#2]{%
  \@ifnextchar[{\principaladvisor@ii{#1}[#2]}{\principaladvisor@ii{#1}[#2][\"{O}zye\u{g}\.{i}n University]}%]
}
\def\principaladvisor@ii#1[#2][#3]{%
\ifx\empty#1\empty\else\def\@advisorforabstract{#1}%
    \rightappenditem#1\to\@principaladvisor%
    \rightappenditem#2\to\@principaladvisor%
    \rightappenditem#3\to\@principaladvisor%
    \fi
}          

% Define \secondadvisor{} to take two optional arguments after the
% name. Thus, the usage is 
%    \secondadvisor{Advisor Name}[Advisor Unit][Advisor Institution]
% Advisor Unit defaults to \@department and Advisor Institution
% defaults to \"{O}zye\u{g}in University.
\newcommand{\secondadvisor}[1]{%
  \@ifnextchar[{\secondadvisor@i{#1}}{\secondadvisor@i{#1}[\@department]}%] 
}
\def\secondadvisor@i#1[#2]{%
  \@ifnextchar[{\secondadvisor@ii{#1}[#2]}{\secondadvisor@ii{#1}[#2][\"{O}zye\u{g}\.{i}n University]}%]
}
\def\secondadvisor@ii#1[#2][#3]{%
\ifx\empty#1\empty\else\def\@secondadvisorforabstract{#1}%
    \rightappenditem#1\to\@secondadvisor%
    \rightappenditem#2\to\@secondadvisor%
    \rightappenditem#3\to\@secondadvisor%
    \fi
}          
    

%
%% Committee Chair
%
% Define \committeechair{} to take two optional arguments after the
% name. Thus, the usage is 
%    \committeechair{Name}[Unit][Institution]
% Unit defaults to \@department and Institution defaults to Georgia
% Institute of Technology.
\newcommand{\committeechair}[1]{%
  \@ifnextchar[{\committeechair@i{#1}}{\committeechair@i{#1}[\@department]}%]
}
\def\committeechair@i#1[#2]{%
  \@ifnextchar[{\committeechair@ii{#1}[#2]}{\committeechair@ii{#1}[#2][\"{O}zye\u{g}\.{i}n University]}%]
}
\def\committeechair@ii#1[#2][#3]{%
\ifx\empty#1\empty\else\rightappenditem#1\to\@committeechair%
    \rightappenditem#2\to\@committeechair%
    \rightappenditem#3\to\@committeechair%
    \fi
}          

%
%% Committee Members
%
% Define \{first|second|third|fourth|fifth|sixth}member{} to take two
% optional arguments after the name. Thus, the usage is 
%    \*member{Member Name}[Member Unit][Member Institution]
% Member Unit defaults to \@department and Member Institution
% defaults to \"{O}zye\u{g}in University.
\def\advisor[1]{}

\newcommand{\firstmember}[1]{%
  \@ifnextchar[{\firstmember@i{#1}}{\firstmember@i{#1}[\@department]}%]
}
\def\firstmember@i#1[#2]{%
  \@ifnextchar[{\firstmember@ii{#1}[#2]}{\firstmember@ii{#1}[#2][\"{O}zye\u{g}\.{i}n University]}%]
}
\def\firstmember@ii#1[#2][#3]{%
\ifx\empty#1\empty\else\rightappenditem#1\to\@firstmember%
    \rightappenditem#2\to\@firstmember%
    \rightappenditem#3\to\@firstmember%
    \fi
}          

\newcommand{\secondmember}[1]{%
  \@ifnextchar[{\secondmember@i{#1}}{\secondmember@i{#1}[\@department]}%]
}
\def\secondmember@i#1[#2]{%
  \@ifnextchar[{\secondmember@ii{#1}[#2]}{\secondmember@ii{#1}[#2][\"{O}zye\u{g}\.{i}n University]}%]
}
\def\secondmember@ii#1[#2][#3]{%
\ifx\empty#1\empty\else\rightappenditem#1\to\@secondmember%
    \rightappenditem#2\to\@secondmember%
    \rightappenditem#3\to\@secondmember%
    \fi
}          

\newcommand{\thirdmember}[1]{%
  \@ifnextchar[{\thirdmember@i{#1}}{\thirdmember@i{#1}[\@department]}%]
}
\def\thirdmember@i#1[#2]{%
  \@ifnextchar[{\thirdmember@ii{#1}[#2]}{\thirdmember@ii{#1}[#2][\"{O}zye\u{g}\.{i}n University]}%]
}
\def\thirdmember@ii#1[#2][#3]{%
\ifx\empty#1\empty\else\rightappenditem#1\to\@thirdmember%
    \rightappenditem#2\to\@thirdmember%
    \rightappenditem#3\to\@thirdmember%
    \fi
}          

\newcommand{\fourthmember}[1]{%
  \@ifnextchar[{\fourthmember@i{#1}}{\fourthmember@i{#1}[\@department]}%]
}
\def\fourthmember@i#1[#2]{%
  \@ifnextchar[{\fourthmember@ii{#1}[#2]}{\fourthmember@ii{#1}[#2][\"{O}zye\u{g}\.{i}n University]}%]
}
\def\fourthmember@ii#1[#2][#3]{%
\ifx\empty#1\empty\else\rightappenditem#1\to\@fourthmember%
    \rightappenditem#2\to\@fourthmember%
    \rightappenditem#3\to\@fourthmember%
    \fi
}          

\newcommand{\fifthmember}[1]{%
  \@ifnextchar[{\fifthmember@i{#1}}{\fifthmember@i{#1}[\@department]}%]
}
\def\fifthmember@i#1[#2]{%
  \@ifnextchar[{\fifthmember@ii{#1}[#2]}{\fifthmember@ii{#1}[#2][\"{O}zye\u{g}\.{i}n University]}%]
}
\def\fifthmember@ii#1[#2][#3]{%
\ifx\empty#1\empty\else\rightappenditem#1\to\@fifthmember%
    \rightappenditem#2\to\@fifthmember%
    \rightappenditem#3\to\@fifthmember%
    \fi
}          

\newcommand{\sixthmember}[1]{%
  \@ifnextchar[{\sixthmember@i{#1}}{\sixthmember@i{#1}[\@department]}%]
}
\def\sixthmember@i#1[#2]{%
  \@ifnextchar[{\sixthmember@ii{#1}[#2]}{\sixthmember@ii{#1}[#2][\"{O}zye\u{g}\.{i}n University]}%]
}
\def\sixthmember@ii#1[#2][#3]{%
\ifx\empty#1\empty\else\rightappenditem#1\to\@sixthmember%
    \rightappenditem#2\to\@sixthmember%
    \rightappenditem#3\to\@sixthmember%
    \fi
}          

%
%% bibliography databases
%
\newcommand{\bibfiles}[1]%
  {\ifx\empty#1\empty\else\gdef\@bibfiles{#1}\fi}

%
%% default values of private functions
%
\def\@title{}
\def\@author{}
\def\@bibfiles{}
\def\@mainadvisor{}
\def\@coadvisor{}
\def\@principaladvisor{}
\def\@secondadvisor{}
\def\@committeechair{}
\def\@firstmember{}
\def\@secondmember{}
\def\@thirdmember{}
\def\@fourthmember{}
\def\@fifthmember{}
\def\@sixthmember{}
\def\@submitdate{\ifcase\the\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi
  \space \number\the\year}
\def\@copyrightyear{\number\the\year}
\def\@bibfiles{}

%% Switch for printing copyright notice on titlepage
%
\newif\ifcopyright
\copyrighttrue % initially true by default

%% Switch for generating a title page
%
\newif\iftitlepage
\titlepagetrue % initially true by default

%% Switch for generating a signature page
%
\newif\ifsignaturepage
\signaturepagetrue % initially true by default

%% Switch for generating a list of figures
%
\newif\iffigurespage
\figurespagetrue % initially true by default

%% Switch for generating a list of tables
%
\newif\iftablespage
\tablespagetrue % initially true by default

%% Switch for generating a table of contents
%
\newif\ifcontentspage
\contentspagetrue % initially true by default

%% Switch for generating a bibliography
%
\newif\ifbibpage
\bibpagetrue % initially true by default

%% Switch to indicate whether chapters are \input{}'ed or
%% \include{}'ed.  Not currently used.
%
\newif\ifusinginclude
\usingincludefalse % initially false by default -- document uses \input{}

%% Switch for relaxing the strict margin requirements 
%% on the title page and signature page.  Default is to
%% rigidly adhere to the standard (but that's ugly)
%
\newif\ifstrictmargins
\strictmarginstrue % initially true by default

%% Switch for printing DEDICATION across the top of the dedication page
%
\newif\ifdedicationheading
\dedicationheadingfalse % initially false by default

%% Switch for indicating that the thesis has multiple volumes
%
\newif\ifmultivolume
\multivolumefalse % initially false by default

%%%%%%    Front Matter Commands and Environments
%%
%% \beforepreface
%%   --- create title, signature page
%%   --- redefined the \maketitle command here, but
%%       don't call it directly.  Use \beforepreface.
%%
%%   \begin{dedication}...\end{dedication}
%%   \begin{preface}...\end{preface}
%%   \begin{acknowledgements}...\end{acknowlegments}
%%   \prefacesection{other-title}
%%     --- followed by section text
%%   \contents
%%     --- prints table of contents, figures, and tables
%%   \begin{abstract}...\end{abstract}  
%% \afterpreface

\newcommand{\title@top}{%
  \ifstrictmargins
    \begin{center}%
        {\fontsize{15}{1}\bfseries\MakeUppercase{\expandafter{\@title}}}\\%%%% TITLE FONT SIZE!!!!
    \end{center}%
  \else%
    \begin{center}
%     \vspace*{\stretch{1}}
        {\large\bfseries\MakeUppercase{\expandafter{\@title}}}%%%%% TITLE FONT SIZE AGAIN
    \end{center}%
  \fi%
}

\newcommand{\title@text}{
  \begin{center}
    \fontsize{14}{12}\textbf{
    by\\
    \vspace{0.2cm}
    {\large\bfseries{\expandafter{\@author}}}\\
    }
    \vspace*{90pt}
    \ifdissertation Dissertation\else Thesis\fi\\
    Submitted in Partial Fulfillment of the \\
    Requirements for the Degree of
    \vspace*{50pt} \\
    \fontsize{14}{12}\textit{\@degree} \vspace*{50pt} \\ in
       \\ {\@department}\\
       \vspace{50pt}
       Advisor: {\@mainadvisor} \\
       \ifcoadvisor Co-Advisor: {\@coadvisor}\else \fi \\
       \vspace{44pt}
    {\@faculty} \\
    \"{O}zye\u{g}\.{i}n University\\
    İstanbul \\
    \vspace{30pt}
    {\@submitdate}%
  \end{center}
}

\newcommand{\make@parttitle}[1]{%if argument is present, it's the part title 
  \begingroup
    \newlinestretch{1}%
    \phantomsection%
    \title@top
    \ifstrictmargins
      \vspace*{0.5in}
      \begin{center}
        \begin{doublespaced}{\bfseries%
          \expandafter{\Makeuppercase{\partname}\space\Makeuppercase{\thepart}}\\
          \ifx\@empty#1\@empty\else%
            \expandafter{#1}\\
          \fi%
        }\end{doublespaced}
        \ \\
        by\\ 
        \ \\ 
        {{\large\bfseries{\expandafter\@author}}}\\
      \end{center}%
      \vfill
    \else%
      \vspace*{0.5in}
      \begin{center}
        \begin{doublespaced}{\Huge\bfseries%
          \expandafter{\Makeuppercase{\partname}\space\Makeuppercase{\thepart}}\\
          \ifx\@empty#1\@empty\else%
            \expandafter{#1}\\
          \fi%
        }\end{doublespaced}
        \vspace*{1.35in}
        \ \\
        by\\
        \ \\
        {\Large\bfseries{\@author}}\\
      \end{center}%
      \vfill
    \fi%
  \endgroup%
}%makeparttitle

\renewcommand{\maketitle}{%
  %\interlinepenalty \@M
  \normalfont
  \begingroup
    \newlinestretch{1}%
    \begingroup
    \phantomsection%
      \pdfbookmark[0]{Coverpage}{coverpage}%
    \centering
    \vspace*{42pt}
    \fontsize{15}{12}\bfseries\MakeUppercase{\@title}\\
        \vspace*{200pt}
    {\normalsize\bfseries\MakeUppercase{\expandafter{\@author}}} \\
        \vspace*{270pt}
        \normalsize\Makeuppercase{\textbf{\"{O}zye\u{g}\.{i}n University}}\\
    \vspace*{18pt}
    \Makeuppercase{\@submitdate}%
    \setcounter{page}{0}
    \newpage
    \endgroup
    \begin{titlepage}%
      \phantomsection%
      \pdfbookmark[0]{Titlepage}{title}%
      \title@top%
      \ifstrictmargins%
        \vspace{50pt}
        \title@text% contains a \vfill between \degree and \department
      \else%
        \vfill%\vspace*{1.35in}
        \title@text% contains a \vfill between \degree and \department
        \vspace*{.2in}%
      \fi%
      \setcounter{page}{1}%
    \end{titlepage}% this has a \newpage
  \endgroup%
  \setcounter{page}{2}%
}%maketitle

%
%% \begin{dedication}...\end{dedication} formats a
%% dedication section
%
%
\newcommand{\dedicationtop}{\vspace{0.1cm}}%*{\stretch{1}}}
\newcommand{\dedicationbottom}{\bigskip\bigskip\vspace*{\stretch{1}}}
\newenvironment{dedication}{%
  \typeout{*****************    Dedication    ******************}
  \if@openright\cleardoublepage\else\clearpage\fi 
  \phantomsection%
 % \addcontentsline{toc}{chapter}%
  %  {\texorpdfstring{\Makeuppercase{Dedication}}{Dedication}}
  \ifdedicationheading
    \chapter*{\MakeUppercase{Dedication}}
  \else
    \chapter*{}
  \fi
  \vskip 0.5in
  \begingroup
  \begin{itshape}\dedicationtop
  \thispagestyle{empty}
}{\dedicationbottom\end{itshape}\par\endgroup}%dedication
%
%% \begin{acknowledgements}...\end{acknowledgements} formats an
%% acknowledgements section
%
\newenvironment{acknowledgements}{%
  \typeout{***************** Acknowledgements ******************}
  \if@openright\cleardoublepage\else\clearpage\fi 
  \phantomsection%
  \addcontentsline{toc}{chapter}%
    {\texorpdfstring{\Makeuppercase{Acknowledgements}}{Acknowledgements}}
  %\chapter*{\MakeUppercase{Acknowledgements}}
   \chapter*{\MakeUppercase{\textbf {\fontsize{15}{15}\selectfont Acknowledgements}}}
  \begingroup
}{\par\endgroup}%Acknowledgements
%
%% \begin{abstract}...\end{abstract} formats an
%% abstract section
%
%% Change \begin{abstract}...\end{abstract} to follow guidelines
%% and put the abstract on a separate page (checking @openright).
%
\newenvironment{originality}{%
  \typeout{*****************      Declaration of Originality     ******************}
  \if@openright\cleardoublepage\else\clearpage\fi 
  \phantomsection%
  \addcontentsline{toc}{chapter}%
    {\texorpdfstring{\Makeuppercase{Declaration of Originality}}{Declaration of Originality}}
  %\chapter*{\MakeUppercase{Declaration of Originality}}
  \chapter*{\MakeUppercase{\textbf {\fontsize{15}{15}\selectfont Declaration of Originality}}}
  \begingroup
}{\endgroup
\hspace*{-0.3in}
%{\parbox[t]{\signature@width}{%
 %    \vspace*{0.5in} \rule{\signature@width}{.01in}\\
  %    \@author
   %   \parbox[t]{\signature@width}{\begin{raggedright} \hfill\\
    %    \hfill\\
     %   \end{raggedright}\hfill}\\
      %\vspace{12pt}%
    %}
}%Declaration of Originality

\renewenvironment{abstract}{%
  \typeout{*****************      Abstract     ******************}
  \if@openright\cleardoublepage\else\clearpage\fi 
  \phantomsection%
  \addcontentsline{toc}{chapter}%
    {\texorpdfstring{\Makeuppercase{Abstract}}{Abstract}}
  %\chapter*{\MakeUppercase{Abstract}}
  \chapter*{\MakeUppercase{\textbf {\fontsize{15}{15}\selectfont Abstract}}}
  \begingroup
}{\par\endgroup}%abstract

%% \begin{ozetce}...\end{ozetce} formats an
%% preface section
%
\newenvironment{ozetce}{%
  \typeout{*****************      Ozetce     ******************}
  \if@openright\cleardoublepage\else\clearpage\fi 
  \phantomsection%
  \addcontentsline{toc}{chapter}%
    {\texorpdfstring{\Makeuppercase{\"{O}zet}}{\"{O}zet}}
  %\chapter*{\MakeUppercase{\"{O}zet\c{c}e}}
  \chapter*{\MakeUppercase{\textbf {\fontsize{15}{15}\selectfont \"{O}zet}}}
  \begingroup
}{\par\endgroup}%ozetce



%
%% stuff to generate a signature page
%
\newlength{\signature@width}
\setlength{\signature@width}{3.3in}
\let\signature@body\signature@bodyonecol
\newcounter{signatures}
\newcounter{cnt@Lsig}
\newcounter{cnt@Rsig}
\def\R@signatures{}
\def\L@signatures{}

% Fun stuff from the TeXbook
\toksdef\ta=0 \toksdef\tb=2 % token list registers for temp use
\long\def\leftappenditem#1\to#2{\ta={\\{#1}}\tb=\expandafter{#2}%
  \edef#2{\the\ta\the\tb}}
\long\def\rightappenditem#1\to#2{\ta={\\{#1}}\tb=\expandafter{#2}%
  \edef#2{\the\tb\the\ta}}
\def\concatenate#1=#2&#3{\ta=\expandafter{#2}\tb=\expandafter{#3}%
  \edef#1{\the\ta\the\tb}}
\def\GTlop#1\to#2{\expandafter\GTlopoff#1\GTlopoff#1#2}
\long\def\GTlopoff\\#1#2\GTlopoff#3#4{\def#4{#1}\def#3{#2}}

\newcommand{\dosiglist}[2]{%
  \GTlop#1\to\@@sig \@@sig
  \GTlop#1\to\@@sig \@@sig
  \GTlop#1\to\@@sig \@@sig
  % we know that cnt@Lsig is at least 3, maybe 4. 5 is right out.
  \ifnum \value{#2} = 4
    \GTlop#1\to\@@sig \@@sig
  \fi
}

\newcommand{\signature}[1]{%
  \ifx\empty#1{}\empty%
  \else%
    \parbox[t]{\signature@width}{%
     \vspace*{0.5in} \rule{\signature@width}{.01in}\\
      \GTlop#1\to\signame%
      \GTlop#1\to\sigdept%
      \GTlop#1\to\siginst%
      \parbox[t]{\signature@width}{\begin{raggedright}\signame \hfill\\
        \sigdept\hfill\\
        \emph{\siginst} \end{raggedright}\hfill}\\
      \vspace{12pt}%
    }
  \fi%
}

\newcommand{\signature@bodyonecol}{%
  \begin{flushleft}
    \parbox{\signature@width}{\begin{flushleft}Approved by:\\ \end{flushleft}}\\
    \vspace*{1in}
    \ifx\empty\@committeechair{}\empty%
    \else%
        \signature{\@committeechair}%
    \fi%
    \ifx\empty\@principaladvisor{}\empty%
    \else%
      \signature{\@principaladvisor}%
    \fi%
    \ifx\empty\@secondadvisor{}\empty%
    \else%
      \signature{\@secondadvisor}%
    \fi%
    \signature\@firstmember
    \signature\@secondmember
    \signature\@thirdmember
    \signature\@fourthmember
    \signature\@fifthmember
    \signature\@sixthmember
    \vspace{.5in}
    \hspace{8cm}\parbox{\signature@width}{\begin{flushleft}Approval Date: \@approveddate\end{flushleft}}\\   
  \end{flushleft}
}

\newcommand{\signature@bodytwocol}{%
  \begin{flushleft}
    Approved by:\\
  \vspace*{12pt}
  \GTlop\L@signatures\to\@@sigLone%
  \GTlop\L@signatures\to\@@sigLtwo%
  \GTlop\L@signatures\to\@@sigLthree%
  \ifnum\value{cnt@Lsig}=4
     \GTlop\L@signatures\to\@@sigLfour
     \else\def\@@sigLfour{}
  \fi

  \GTlop\R@signatures\to\@@sigRone%
  \GTlop\R@signatures\to\@@sigRtwo%
  \ifnum\value{cnt@Rsig}=2
     \def\@@sigRthree{}
     \def\@@sigRfour{Approval Date: \@approveddate}
   \fi
  \ifnum\value{cnt@Rsig}=3
      \GTlop\R@signatures\to\@@sigRthree%
      \def\@@sigRfour{Approval Date: \@approveddate}
  \fi
  \ifnum\value{cnt@Rsig}=4
      \GTlop\R@signatures\to\@@sigRthree%
      \GTlop\R@signatures\to\@@sigRfour%
  \fi

  \begin{tabular*}{\textwidth}[t]{@{\extracolsep{\fill}}ll}
    \@@sigLone & \@@sigRone \\ %
    \@@sigLtwo & \@@sigRtwo\\ %
    \@@sigLthree & \@@sigRthree\\ %
    \@@sigLfour & \@@sigRfour \\
     \ifnum\value{cnt@Rsig}=4
        \space &%
        Approval Date: \@approveddate
     \fi
  \end{tabular*}
  \end{flushleft}
}

\def\add@Lsig#1{
  \ifx#1\@empty\relax\else%
    \rightappenditem#1\to\L@signatures
    \addtocounter{cnt@Lsig}{1}%
  \fi
}
\def\add@Rsig#1{%
  \ifx\@empty#1\relax\else
    \rightappenditem#1\to\R@signatures
    \addtocounter{cnt@Rsig}{1}%
  \fi
}
\newcommand{\makesignature}{%
  \if@openright\cleardoublepage\else\clearpage\fi 
  \phantomsection%
  \pdfbookmark[0]{Signatures}{signatures}%
  % do not addtocontents (although it is in bookmarklist)
  \ifx\@empty\@committeechair\relax\else
    \addtocounter{signatures}{1}%
        \GTlop\@committeechair\to\z%
        \leftappenditem{\z, \mbox{Committee Chair}}\to\@committeechair%
    \add@Lsig{\signature{\@committeechair}}
  \fi
  \ifx\@empty\@principaladvisor\relax\else
    \addtocounter{signatures}{1}%
      \GTlop\@principaladvisor\to\a%
      \leftappenditem{\a, \advis@r}\to\@principaladvisor%      
    \add@Lsig{\signature{\@principaladvisor}}
  \fi
    \ifx\@empty\@secondadvisor\relax\else
    \addtocounter{signatures}{1}%
      \GTlop\@secondadvisor\to\a%
      \leftappenditem{\a, Co-\advis@r}\to\@secondadvisor%      
    \add@Lsig{\signature{\@secondadvisor}}
  \fi
  \ifx\@empty\@firstmember\relax\else
    \addtocounter{signatures}{1}%
    \add@Lsig{\signature\@firstmember}
  \fi
% The first three will ALWAYS be in the left column, but now we must compute
% the total number of sigs before doing anything else.
  \ifx\@empty\@secondmember\relax\else\addtocounter{signatures}{1}\fi
  \ifx\@empty\@thirdmember\relax\else\addtocounter{signatures}{1}\fi
  \ifx\@empty\@fourthmember\relax\else\addtocounter{signatures}{1}\fi
  \ifx\@empty\@fifthmember\relax\else\addtocounter{signatures}{1}\fi
  \ifx\@empty\@sixthmember\relax\else\addtocounter{signatures}{1}\fi
  \typeout{SIGNATURES: \arabic{signatures}}
  \ifnum \value{signatures} < 5 % fuggeddaboutit.  Only one column
    \let\signature@body\signature@bodyonecol
    \setlength{\signature@width}{0.52\textwidth}
  \else
    \let\signature@body\signature@bodytwocol
    \setlength{\signature@width}{0.46\textwidth}
    \newcounter{halfsig}
    \setcounter{halfsig}{\value{signatures} - (\value{signatures} / 2)}
    \typeout{LEFTCNT: \arabic{cnt@Lsig}  HALF: \arabic{halfsig}}
    \ifnum \value{cnt@Lsig} < \value{halfsig}
      \add@Lsig{\signature\@secondmember}
      \ifnum \value{cnt@Lsig} < \value{halfsig}
        \ifx\@empty\@thirdmember\relax\else\add@Lsig{\signature\@thirdmember}\fi % can't ever have more than this in left column
        \ifx\@empty\@fourthmember\relax\else\add@Rsig{\signature\@fourthmember}\fi
        \ifx\@empty\@fifthmember\relax\else\add@Rsig{\signature\@fifthmember}\fi
        \ifx\@empty\@sixthmember\relax\else\add@Rsig{\signature\@sixthmember}\fi
      \else
        \ifx\@empty\@thirdmember\relax\else\add@Rsig{\signature\@thirdmember}\fi
        \ifx\@empty\@fourthmember\relax\else\add@Rsig{\signature\@fourthmember}\fi
        \ifx\@empty\@fifthmember\relax\else\add@Rsig{\signature\@fifthmember}\fi
        \ifx\@empty\@sixthmember\relax\else\add@Rsig{\signature\@sixthmember}\fi
      \fi
    \else
      \ifx\@empty\@secondmember\relax\else\add@Rsig{\signature\@secondmember}\fi
      \ifx\@empty\@thirdmember\relax\else\add@Rsig{\signature\@thirdmember}\fi
      \ifx\@empty\@fourthmember\relax\else\add@Rsig{\signature\@fourthmember}\fi
      \ifx\@empty\@fifthmember\relax\else\add@Rsig{\signature\@fifthmember}\fi
      \ifx\@empty\@sixthmember\relax\else\add@Rsig{\signature\@sixthmember}\fi
    \fi   
  \fi
  \title@top
  \ifx\@empty\@coadvisor\relax\else
  \fi
  \vspace{60pt}
  \begin{flushleft}
    \signature@body
    \ifstrictmargins\relax\else
      \vspace{.2in}
      \mbox{}
    \fi
  \end{flushleft}
  \thispagestyle{empty}
}
%
%% beforepreface
%
\newcommand{\beforepreface}{%
  \newlinestretch{1.0}%
  \pagenumbering{roman}%
  \pagestyle{\front@pagestyle}%
  \iftitlepage%
    \maketitle%
  \fi%
  \ifmultivolume%
    \part{}%
  \fi%
  \ifsignaturepage%
    \makesignature%
  \fi%
  \newlinestretch{\@spacing}%
}
%
%% \prefacesection is here for backward compatibility with
%% the GT-thesis.sty package, and to add preface sections
%% that are not already defined.  For Abstract, Preface,
%% Dedication, and Acknowledgements sections, use the 
%% appropriate environments: \begin{abstract}...\end{abstract}
%% etc.
%
\newcommand{\prefacesection}[1]{%
  \if@openright\cleardoublepage\else\clearpage\fi 
  \phantomsection%
  \addcontentsline{toc}{chapter}%
    {\texorpdfstring{\Makeuppercase{#1}}{#1}}
  \newlinestretch{\@spacing}
  \chapter*{\MakeUppercase{#1}}
  \vskip 0.5in
}
\newcommand{\afterpreface}{%
  \if@draft%
  \else%
    \if@twoside%
      \if@openright%
        \cleardoublepage%
      \fi%
    \fi%
  \fi%
  \newpage%
  \pagenumbering{arabic}%
  \pagestyle{\body@pagestyle}%
  \newlinestretch{\@spacing}%
}

% dummy commands to prevent recursion errors...
\newcommand{\gtcontentsname}{}
\newcommand{\toccontentlinestring}{}
\newcommand{\tocpdfbookmarkstring}{}
\newcommand{\gtlistfigurename}{}
\newcommand{\lofcontentlinestring}{}
\newcommand{\lofpdfbookmarkstring}{}
\newcommand{\gtlisttablename}{}
\newcommand{\lotcontentlinestring}{}
\newcommand{\lotpdfbookmarkstring}{}

\newcommand{\settocstring}[1]{%
  \renewcommand{\gtcontentsname}{#1}
  \renewcommand{\contentsname}{\Makeuppercase{#1}}
  \renewcommand{\toccontentlinestring}{%
    \texorpdfstring{\Makeuppercase{#1}}{#1}
  }
  \renewcommand{\tocpdfbookmarkstring}{#1}
}
\newcommand{\setlofstring}[1]{%
  \renewcommand{\gtlistfigurename}{#1}
  \renewcommand{\listfigurename}{\Makeuppercase{#1}}
  \renewcommand{\lofcontentlinestring}{%
    \texorpdfstring{\Makeuppercase{#1}}{#1}
  }
  \renewcommand{\lofpdfbookmarkstring}{#1}
}
\newcommand{\setlotstring}[1]{%
  \renewcommand{\gtlisttablename}{#1}
  \renewcommand{\listtablename}{\Makeuppercase{#1}}
  \renewcommand{\lotcontentlinestring}{%
    \texorpdfstring{\Makeuppercase{#1}}{#1}
  }
  \renewcommand{\lotpdfbookmarkstring}{#1}
}
\settocstring{Table of Contents}
\setlofstring{List of Figures}
\setlotstring{List of Tables}

%
%% All this junk is for handling the spacing in the TOC, LOF, and LOT.
%
\newlength{\gt@tocentryskip@value}
\newlength{\gt@beforepartskip@value}
\newlength{\gt@beforechapskip@value}
\newlength{\gt@beforesecskip@value}
\newlength{\gt@beforesubsecskip@value}
\newlength{\gt@beforesubsubsecskip@value}
\newlength{\gt@beforeparaskip@value}
\newlength{\gt@beforesubparaskip@value}
\newlength{\gt@beforefigskip@value}
\newlength{\gt@beforetableskip@value}

\def\set@gttocskip#1{%
  \setlength{\gt@tocentryskip@value}{#1}
  % set base lengths
  \setlength{\gt@beforepartskip@value}{2\gt@tocentryskip@value}
  \setlength{\gt@beforechapskip@value}{1.5\gt@tocentryskip@value}
  \setlength{\gt@beforesecskip@value}{\gt@tocentryskip@value}
  \setlength{\gt@beforesubsecskip@value}{\gt@tocentryskip@value}
  \setlength{\gt@beforesubsubsecskip@value}{\gt@tocentryskip@value}
  \setlength{\gt@beforeparaskip@value}{\gt@tocentryskip@value}
  \setlength{\gt@beforesubparaskip@value}{\gt@tocentryskip@value}
  \setlength{\gt@beforefigskip@value}{\gt@tocentryskip@value}
  \setlength{\gt@beforetableskip@value}{\gt@tocentryskip@value}
  % add glue
  \addtolength{\gt@beforepartskip@value}{\z@ \@plus\p@}
  \addtolength{\gt@beforechapskip@value}{\z@ \@plus\p@}
  \addtolength{\gt@beforesecskip@value}{\z@ \@plus.2\p@}
  \addtolength{\gt@beforesubsecskip@value}{\z@ \@plus.2\p@}
  \addtolength{\gt@beforesubsubsecskip@value}{\z@ \@plus.2\p@}
  \addtolength{\gt@beforeparaskip@value}{\z@ \@plus.2\p@}
  \addtolength{\gt@beforesubparaskip@value}{\z@ \@plus.2\p@}
  \addtolength{\gt@beforefigskip@value}{\z@ \@plus.2\p@}
  \addtolength{\gt@beforetableskip@value}{\z@ \@plus.2\p@}
}
\set@gttocskip{10pt}

% gobble the pagenumber
\newcommand*{\l@part@pagenumfont}[1]{}
% note: we don't do the fancy volume title centering here, because
% we use {part} for the \labelchaptersintableofcontents stuff.  And
% that is NOT centered.
\renewcommand*{\l@part}[2]{%
  \ifnum \c@tocdepth >-2\relax
    \addpenalty{-\@highpenalty}%
    \addvspace{\gt@beforepartskip@value}%
    \setlength\@tempdima{3em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \interlinepenalty\@M
      {\leavevmode #1\hfil \hb@xt@\@pnumwidth{\hss \l@part@pagenumfont{#2}}}\par
       \nobreak
         \global\@nobreaktrue
         \everypar{\global\@nobreakfalse\everypar{}}%
    \endgroup
  \fi}
\newcommand*{\gt@dottedtocline}[5]{%
  \ifnum #1>\c@tocdepth \else
    \addvspace{\gt@@toclineskip}
    {\leftskip #2\relax \rightskip \@tocrmarg \parfillskip -\rightskip
     \parindent #2\relax\@afterindenttrue
     \interlinepenalty\@M
     \leavevmode
     \@tempdima #3\relax
     \advance\leftskip \@tempdima \null\nobreak\hskip -\leftskip
     {#4}\nobreak
     \leaders\hbox{$\m@th
        \mkern \@dotsep mu\hbox{.}\mkern \@dotsep
        mu$}\hfill
     \nobreak
     \hb@xt@\@pnumwidth{\hfil\normalfont \normalcolor #5}%
     \par}%
  \fi}
\renewcommand*\l@chapter[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \addvspace{\gt@beforechapskip@value}%
    \setlength\@tempdima{2em}% was 1.5em, but that's too small.  Add 0.5em to all others
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode %\bfseries %change to normal font 10/11/2024
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      #1\nobreak\normalfont\normalcolor
      \leaders\hbox{$\m@th
        \mkern \@dotsep mu\hbox{.}\mkern \@dotsep
	mu$}\hfill
      \nobreak
%      \hb@xt@\@pnumwidth{\hss\bfseries #2}
      \hb@xt@\@pnumwidth{\hss #2} %change to normal font 10/11/2024
      \par
      \penalty\@highpenalty
    \endgroup
  \fi}
\renewcommand*\l@section{%
  \let\gt@@toclineskip=\gt@beforesecskip@value
  \gt@dottedtocline{1}{2.0em}{2.3em}}
\renewcommand*\l@subsection{%
  \let\gt@@toclineskip=\gt@beforesubsecskip@value
  \gt@dottedtocline{2}{4.3em}{3.2em}}
\renewcommand*\l@subsubsection{%
  \let\gt@@toclineskip=\gt@beforesubsubsecskip@value
  \gt@dottedtocline{3}{7.5em}{4.1em}}
\renewcommand*\l@paragraph{%
  \let\gt@@toclineskip=\gt@beforeparaskip@value
  \gt@dottedtocline{4}{10.5em}{5em}}
\renewcommand*\l@subparagraph{%
  \let\gt@@toclineskip=\gt@beforesubparaskip@value
  \gt@dottedtocline{5}{12.5em}{6em}}
\renewcommand*\l@figure{%
  \let\gt@@toclineskip=\gt@beforefigskip@value
  \gt@dottedtocline{1}{1.5em}{2.3em}}% this is indented 1.5em so that 
                                     % if you wish, you can a 'Figure' header
                                     % centered above the numbers using \addtocontents
\renewcommand*\l@table{%
 \let\gt@@toclineskip=\gt@beforetableskip@value
  \gt@dottedtocline{1}{1.5em}{2.3em}}% ditto

  

\newlength{\gt@tmpa}
\newcommand{\do@figurespage}{%
  \iffigurespage
    \if@openright\cleardoublepage\else\clearpage\fi 
    % must clear page here, so that phantomsection\addcontentsline is on the correct page
    \phantomsection%
    \addcontentsline{toc}{chapter}{\lofcontentlinestring}
    \settoheight{\gt@tmpa}{A}
    \set@gttocskip{\gt@tmpa}
    {\newlinestretch{1}
     \listoffigures
    }
    \newpage
  \fi
}
\newcommand{\do@tablespage}{%
  \iftablespage
    \if@openright\cleardoublepage\else\clearpage\fi 
    % must clear page here, so that phantomsection\addcontentsline is on the correct page
    \phantomsection%
    \addcontentsline{toc}{chapter}{\lotcontentlinestring}
    \settoheight{\gt@tmpa}{A}
    \set@gttocskip{\gt@tmpa}
    {\newlinestretch{1}
     \listoftables
    }
    \newpage
  \fi
}
\newcommand{\do@contentspage}{%
  \ifcontentspage
    \if@openright\cleardoublepage\else\clearpage\fi 
    % must clear page here, so that phantomsection\addcontentsline is on the correct page
    \phantomsection%
    \pdfbookmark[0]{\tocpdfbookmarkstring}{toc}%
    \settoheight{\gt@tmpa}{A}
    \set@gttocskip{\gt@tmpa}
     {\newlinestretch{1}
     \tableofcontents
     }
     \newpage
  \fi
}
\newcommand{\do@losapage}{}
\newcommand{\do@glossarypage}{}
\newcommand{\do@indexpage}{}

\newcommand{\contents}{%
  \newpage
  \newlinestretch{\@spacing}
  \do@contentspage
  \do@tablespage
  \do@figurespage
  \do@losapage  
  \do@glossarypage  
}

%%%%%%    Main Matter Commands and Environments
%%
%% redefine chapter headings style
%% redefine appendix headings style
%% redefine section headings style
%% number figures and tables sequentially throughout, rather
%%   than restarting for each chapter.  Ditto equations.
%% redefine macro for floats (incl. figures and tables)
%%   so that single spacing is used
%% define a "gtindent" command for paragraph indents:
%%   blank line + six space first line indentation
%% settocdepth - use this to change how "deep" to number 
%%   in the table of contents for different sections; e.g.
%%   subsubsections for chapters, then switch to chapter-only
%%   for appendices.

% This package uses David Carlisle's \@removefromreset command as
% specified in the remreset package available from CTAN as
% macros/latex/contrib/supported/carlisle/remreset.sty
% It is \provided here as a convenience to the user, and with
% David Carlisle's permission.  remreset.sty is licensed under
% the LPPL; David has explicitly given permission to include
% it here, under the GPL.
% START OF DAVID CARLISLE'S CODE

\renewcommand{\@removefromreset}[2]{{%
  \expandafter\let\csname c@#1\endcsname\@removefromreset
  \def\@elt##1{%
    \expandafter\ifx\csname c@##1\endcsname\@removefromreset
    \else
      \noexpand\@elt{##1}%
    \fi}%
  \expandafter\xdef\csname cl@#2\endcsname{%
    \csname cl@#2\endcsname}}}
% END OF DAVID CARLISLE'S CODE
%%%%% See http://www.tex.ac.uk/cgi-bin/texfaq2html?label=running-nos

%
%% Figures and tables are to be numbered sequentially throughout the
%% thesis, rather than within chapters; for style consistency, do
%% equations the same. 
%
%\@removefromreset{figure}{chapter}
%\@removefromreset{table}{chapter}
%\@removefromreset{equation}{chapter}
%\def\thefigure{\@arabic\c@figure}
%\def\thetable{\@arabic\c@table}
%\def\theequation{\arabic{equation}}

%
%% Redefine the macro used for floats (including figures and tables)
%% so that single spacing is used.
%% (Note \def\figure{\@float{figure}set single spacing} doesn't work
%%  because figure has an optional argument)
%%
%% This code was copied directly from latex.ltx, but with the
%% \newlinespacing{} macro added to it.
%
\def\@xfloat #1[#2]{%
  \@nodocument
  \def \@captype {#1}%
   \def \@fps {#2}%
   \@onelevel@sanitize \@fps
   \def \reserved@b {!}%
   \ifx \reserved@b \@fps
     \@fpsadddefault
   \else
     \ifx \@fps \@empty
       \@fpsadddefault
     \fi
   \fi
   \ifhmode
     \@bsphack
     \@floatpenalty -\@Mii
   \else
     \@floatpenalty-\@Miii
   \fi
  \ifinner
     \@parmoderr\@floatpenalty\z@
  \else
    \@next\@currbox\@freelist
      {%
       \@tempcnta \sixt@@n
       \expandafter \@tfor \expandafter \reserved@a
         \expandafter :\expandafter =\@fps
         \do
          {%
           \if \reserved@a h%
             \ifodd \@tempcnta
             \else
               \advance \@tempcnta \@ne
             \fi
           \fi
           \if \reserved@a t%
             \@setfpsbit \tw@
           \fi
           \if \reserved@a b%
             \@setfpsbit 4%
           \fi
           \if \reserved@a p%
             \@setfpsbit 8%
           \fi
           \if \reserved@a !%
             \ifnum \@tempcnta>15
               \advance\@tempcnta -\sixt@@n\relax
             \fi
           \fi
           }%
       \@tempcntb \csname ftype@\@captype \endcsname
       \multiply \@tempcntb \@xxxii
       \advance \@tempcnta \@tempcntb
       \global \count\@currbox \@tempcnta
       }%
    \@fltovf
  \fi
  \global \setbox\@currbox
    \color@vbox
      \normalcolor
      \vbox \bgroup
        \newlinestretch{1.0}
        \hsize\columnwidth
        \@parboxrestore
        \@floatboxreset
}

% Redefine the macro used for caption labels, for a (slightly)
% fancier format.  Feel free to use the caption2 package instead...
\long\def\@makecaption#1#2{%
  \vskip\abovecaptionskip
  \sbox\@tempboxa{\textbf{#1: }#2}%
  \ifdim \wd\@tempboxa >\hsize
    \textsf{\textbf{#1: }}#2\par
  \else
    \global \@minipagefalse
    \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
  \fi
  \vskip\belowcaptionskip}

% Redefine the macro used for footnotes to use single spacing
\long\def\@footnotetext#1{%
  \insert\footins{%
    \newlinestretch{1.0}%
    \footnotesize%
    \interlinepenalty\interfootnotelinepenalty%
    \splittopskip\footnotesep%
    \splitmaxdepth \dp\strutbox \floatingpenalty \@MM%
    \hsize\columnwidth \@parboxrestore%
    \edef\@currentlabel{%
      \csname p@footnote\endcsname\@thefnmark%
    }%
    \@makefntext%
    {\rule{\z@}{\footnotesep}\ignorespaces%
      #1\strut}%
  }%
}

%
%% Paragraph indents (6 spaces)
%% inserts a blank line and then indents the paragraph by 6 spaces
%
\newcommand{\gtindent}{\par \hspace{0.25in}}

%
%% Chapter headings - centered, all caps, chapter number - roman numeral
%
%
%% Use \labelchaptersintableofcontents to insert an entry into the toc
%% that says ``CHAPTERS'' just before Chapter 1.
%  Use \labelappendicesintableofcontents to insert an entry into the toc
%% that says ``APPENDICES'' just before Appendix A.
%
\let\orig@contentsline=\contentsline
\newcommand{\labelchaptersintableofcontents}[1][CHAPTERS]{%
  \addtocontents{toc}{\protect\orig@contentsline{part}{#1}{}}
}
\newcommand{\labelappendicesintableofcontents}[1][APPENDICES]{%
  \addtocontents{toc}{\protect\orig@contentsline{part}{#1}{}}%
}

\renewcommand{\chaptername}{CHAPTER}
\renewcommand{\appendixname}{APPENDIX}
\renewcommand{\thepart}{\@Roman\c@part}
\renewcommand{\partname}{Volume}

%
%% \thegtchapter is used so that we can have ROMAN numbers in the 
%% chapter headings at the beginning of each chapter, but use
%% \thechapter for ARABIC numbers in the running heads on each
%% page within the chapter.
%%
%% You can Change this behavior by redefining \thegtchapter 
%% within your document:
%% \renewcommand{\thegtchapter}{\thechapter}
%
\newcommand{\thegtchapter}{\@arabic\c@chapter}
\renewcommand{\thegtchapter}{\thechapter}
\def\chapapp@tocdepth{\expandafter\chapter@tocdepth}
%
%% The following two def's provide the Indirection needed to work 
%% with hyperref package, since hyperref redefines @chapter and
%% @schapter
%
\def\chapapp@chapter{\chap@chapter}
\def\chapapp@schapter{\chap@schapter}
%
%% Make @chapter and @schapter wrappers for (chap@chapter or app@chapter)
%% and (chap@schapter or app@schapter).  This indirection is necessary to
%% work well with the hyperref package.
%
\def\my@empty{}
\def\@chapter[#1]#2{%
  \def\my@temp{#1}%
  \ifx\my@temp\my@empty
    \chapapp@chapter{#2}
  \else
    \chapapp@chapter[#1]{#2}
  \fi
}
\def\@schapter#1{%
  \chapapp@schapter{#1}
}
%
%% The actual guts of the chapter heading routines
%
\renewcommand{\chapter}{%
  \if@openright\cleardoublepage\else\clearpage\fi
  \if@tcpage% DO NOT use the \front@pagestyle macro here.
    {\thispagestyle{tcplain}}
  \else
    {\thispagestyle{plain}}%report.cls temporarily resets pagestyle to plain. Do the same.
  \fi 
  \settocdepth{\chapapp@tocdepth}
  \global\@topnum\z@
  \@afterindentfalse
  \secdef\@chapter\@schapter
}
\def\chap@chapter[#1]#2{%
  \ifnum \c@secnumdepth >\m@ne
    \refstepcounter{chapter}%
    \typeout{\@chapapp\space\thegtchapter.}%
    \addcontentsline{toc}{chapter}%
      {\texorpdfstring%
        {\protect\numberline{\thegtchapter}\Makeuppercase{#1}}%
        {Chapter \thechapter\space\textemdash\space#1}}%
  \else
    \addcontentsline{toc}{chapter}%
      {\texorpdfstring{\Makeuppercase{#1}}{#1}}%
  \fi
  \chaptermark{#1}%
  \if@twocolumn
    \@topnewpage[\@makechapterhead{#2}]%
  \else
    \@makechapterhead{#2}%
    \@afterheading
  \fi
}
\def\@makechapterhead#1{%
  \ifnum \@marginsize = 4 % oldmargins
    \vspace*{50\p@}%
  \fi
  { \parindent \z@ \raggedright \normalfont
    \ifnum \c@secnumdepth >\m@ne
      \centering \large \bfseries{\thegtchapter.\space\Makeuppercase{#1}}
 %      \centering \large \bfseries \@chapapp\space \thegtchapter     \par\nobreak
    \fi
    \vskip 12\p@
  }
}
\def\chap@schapter#1{%
  \if@twocolumn
    \@topnewpage[\@makeschapterhead{#1}]%
  \else
    \@makeschapterhead{#1}%
    \@afterheading
  \fi
}
\def\@makeschapterhead#1{%
  \ifnum \@marginsize = 4 % oldmargins
    \vspace*{50\p@}%
  \fi
  { \parindent \z@ \raggedright \normalfont
    \interlinepenalty\@M
    \centering \large \bfseries #1\par\nobreak
    \vskip 30\p@
  }
}
%
%% Support for multi-volume thesis.
%%
%% in the premable, set \multivolumetrue and then
%% use the \part{} commannd where you want volume 2 
%% to begin, etc.  Do not give names to your volumes (that is,
%% use ``\part{}'' and not ``\part{Some title}''), because
%% the Graduate Office Guidelines do not allow separate
%% titles for each volume.
%
% we temporarily set the pagenumber to a big negative number, for
% two reasons: 1) so that it doesn't duplicate the other page numbers,
% because the volume title pages are unnumbered and uncounted.  We
% can't merely allow the autoincrement of pagenum and then addtocounter{page}{-1},
% because then both pages would have the same number. 2) it's a BIG negative
% number because we allow it to increment as each \part is declared, so that
% the volume title pages don't duplicate each others pagenums.
\newcounter{part@savepagenum}
\newcounter{part@pagenum}
\setcounter{part@pagenum}{-101} % can't have more than 50 parts,
% but this number must be odd, or twopage dvi's are messed up.
\renewcommand{\part}{%
  \if@openright\cleardoublepage\else\clearpage\fi
  \thispagestyle{empty}%
  \phantomsection%
  \setcounter{part@savepagenum}{\value{page}}
  \setcounter{page}{\value{part@pagenum}}
  \if@twocolumn
    \onecolumn
    \@tempswatrue
  \else
    \@tempswafalse
  \fi
  \secdef\@part\@spart}

\def\@part[#1]#2{%
  \ifnum \c@secnumdepth >-2\relax
    \refstepcounter{part}
    \typeout{\partname\space\thepart.}%
    \addcontentsline{toc}{part}%
      {\texorpdfstring%
        {\noindent\protect\makebox[\@tocrmarg]{}%
          {\protect\makebox[\textwidth - \@tocrmarg - \@tocrmarg]% dadgum \hfill doesn't work without mbox...
          {\hfill\Makeuppercase{\partname}\space\protect{\thepart}\hspace{1em}\Makeuppercase{#1}\hfill}}}%
        {Volume \thepart}}%
  \else
    \addcontentsline{toc}{part}%
    {\texorpdfstring%
      {\Makeuppercase{#1}}%
      {#1}}%
  \fi
  \markboth{}{}
  {\interlinepenalty \@M
     \normalfont
     \ifnum \c@secnumdepth >-2\relax
       \make@parttitle{#1}
     \else
       \make@parttitle{}
     \fi}
     \@endpart}
\def\@spart#1{%
    {\interlinepenalty \@M
     \normalfont
     \make@parttitle{}}
    \@endpart}
\def\@endpart{%
  \vfill\newpage\addtocounter{part@pagenum}{1}%don't count this page
  \if@twoside
    \if@openright
      \null
      \thispagestyle{empty}%
      \newpage\addtocounter{part@pagenum}{1}%if we need to add another page, don't count it either
    \fi
  \fi
  \if@tempswa
    \twocolumn
  \fi
  \setcounter{page}{\value{part@savepagenum}}
}
%
%% Section
%% Heading 1: Large, bold, and italic, at left margin
%% Heading 2: Bold, at left margin
%% Heading 3: Italic, indented 0.25in from left margin
%
\renewcommand{\section}{%
  \@startsection{section}{1}{\z@}%
  {-3.25ex \@plus -1ex \@minus -.2ex}%
  {1.5ex \@plus.2ex}%
  %{\newlinestretch{1}\normalfont\bfseries}
   {\newlinestretch{1}\normalfont\large\bfseries}
}
\renewcommand{\subsection}{%
  \@startsection{subsection}{2}{\z@}%
  {-3.25ex\@plus -1ex \@minus -.2ex}%
  {1.5ex \@plus .2ex}%
  {\newlinestretch{1}\normalfont\normalsize\bfseries\itshape}
  }
\renewcommand{\subsubsection}{%
  \@startsection{subsubsection}{3}{0.25in}%
  {-3.25ex\@plus -1ex \@minus -.2ex}%
  {1.5ex \@plus .2ex}%
  %{\newlinestretch{1}\normalfont\normalsize\itshape}
  {\newlinestretch{1}\normalfont\normalsize\bfseries}
}

\renewcommand{\appendix}{%
  \if@openright
    \cleardoublepage
  \else
    \clearpage
  \fi
  \renewcommand{\@chapapp}{\appendixname}
  \thispagestyle{plain}%    Do NOT use the \back@pagestyle macro here
  \settocdepth{\appendix@tocdepth}
  \setcounter{chapter}{0}%
  \setcounter{section}{0}%
  \def\thechapter{\@Alph\c@chapter}
  \def\chapapp@tocdepth{\expandafter\appendix@tocdepth}
  \def\chapapp@chapter{\app@chapter}
  \def\chapapp@schapter{\app@schapter}
  \renewcommand{\thesection}{\thechapter.\@arabic\c@section}
}
\def\app@chapter[#1]#2{%
  \ifnum \c@secnumdepth >\m@ne
    \refstepcounter{chapter}%
    \typeout{\@chapapp\space\thechapter.}%
    \addcontentsline{toc}{chapter}%
    {\texorpdfstring%
      {\@chapapp\space\protect\numberline{\thechapter}\space---\space\Makeuppercase{#1}}%
      {Appendix\space\thechapter\space\textemdash\space#1}}%must specify "---" explicitly here
  \else
    \addcontentsline{toc}{chapter}{\Makeuppercase{#1}}%
  \fi
  \chaptermark{#1}%
  \if@twocolumn
    \@topnewpage[\@makeapphead{#2}]%
  \else
    \@makeapphead{#2}%
    \@afterheading
  \fi
}
\def\@makeapphead#1{%
  \ifnum \@marginsize = 4 % oldmargins
    \vspace*{50\p@}%
  \fi
  { \parindent \z@ \raggedright \normalfont
    \centering \Large \bfseries \appendixname\space \thechapter. \Makeuppercase{#1}
    \par\nobreak
%    \vskip 30\p@
    \interlinepenalty\@M
    %\centering \Large \bfseries \MakeUppercase{#1}\par\nobreak
    \vskip 30\p@
  }
}
\def\app@schapter#1{%
  \if@twocolumn
    \@topnewpage[\@makesapphead{#1}]%
  \else
    \@makesapphead{#1}%
    \@afterheading
  \fi
}
\def\@makesapphead#1{%
  \ifnum \@marginsize = 4 % oldmargins
    \vspace*{50\p@}%
  \fi
  { \parindent \z@ \raggedright \normalfont
    \interlinepenalty\@M
    \centering \Large \bfseries #1\par\nobreak
    \vskip 30\p@
  }
}
%% end of \appendix environment definitions

%% \settocdepth - use this to change how "deep" to number 
%%   in the table of contents for different sections; e.g.
%%   subsubsections for chapters, then switch to chapter-only
%%   for appendices.
%% tocdepth is reset to the value in \setchaptertocdepth
%%   at each \chapter{}, or to the value in \setappendixtocdepth
%%   at each \chapter{} after the \appendix command.  So, if 
%%   you want to change the defaults, use \setchaptertocdepth and 
%%   \setappendixtocdepth.  To temporarily change depth for the 
%%   current section, use a different function: \settocdepth[x].  
%%   You should never need to call \setcounter{tocdepth}{..} 
%%   directly.
%%
%% 0 = chapter only
%% 1 = chapter + sections
%% 2 = chapter, section, subsection
%% 3 = chapter, section, subsection, subsubsection
%
\newcommand{\settocdepth}[1]{%
  \addtocontents{toc}{\protect\setcounter{tocdepth}{#1}}
}
\newcommand{\setappendixtocdepth}[1]{%
  \def\appendix@tocdepth{#1}
}
\newcommand{\setchaptertocdepth}[1]{%
  \def\chapter@tocdepth{#1}
}

%%%%%%    Back Matter Commands and Environments
%%
%% \beforepostface
%%   \thebibliography redefined so it matches GT's requirements
%%   \begin{vita}...\end{vita}
%%   \postfacesection{other-title}
%%     --- followed by section text
%% \afterpostface
%% \references
%%   --- creates the bibliography
%% \begin{postliminary}...\end{postliminary}
%%   --- preferred to \beforepostface and \afterpostface

% 
%%%%%%    New formatting environments and commands.
%
%% \begin{postliminary} sets the pagestyle for the
%% postliminary sections.  
%%
%% \end{postliminary} resets the pagestyle and
%% performs any other cleanup.
%
\newenvironment{postliminary}%
  {\pagestyle{\back@pagestyle}}%
  {\settocdepth{\chapter@tocdepth}%
   \pagestyle{\body@pagestyle}}

%
%% \begin{vita}...\end{vita} formats a
%% vita section
%
\newenvironment{vita}{%
  \typeout{*****************        Vita       ******************}
  \newlinestretch{\@spacing}
  \if@openright\cleardoublepage\else\clearpage\fi 
  \phantomsection%
  \addcontentsline{toc}{chapter}%
    {\texorpdfstring{\Makeuppercase{Vita}}{Vita}}
  \chapter*{\MakeUppercase{Vita}}
  \@mkboth{\scshape\MakeUppercase{Vita}}%
          {\scshape\MakeUppercase{Vita}}%
  \vskip 0.5in
  \begingroup
}{\par\endgroup}%Vita

\newcommand{\beforepostface}{%
  \pagestyle{\back@pagestyle}
}%

%
%% \postfacesection is here for backward compatibility with
%% the GT-thesis.sty package, and to add postface sections
%% that are not already defined.  (Appendices are not postface
%% material).  Currently, the only predefined postface section
%% is Vita.  Use \begin{vita}...\end{vita}.  (``Index'' is a 
%% postface section, but: it is defined in the add-on style
%% ozu-thesis-index.sty, and it doesn't use \postfacesection.)
%
\newcommand{\postfacesection}[1]{%
  \newlinestretch{\@spacing}
  \if@openright\cleardoublepage\else\clearpage\fi 
  % must clear page here, so that phantomsection\addcontentsline is on the correct page
  \phantomsection%
  \addcontentsline{toc}{chapter}%
    {\texorpdfstring{\Makeuppercase{#1}}{#1}}
  \chapter*{\MakeUppercase{#1}}
  \@mkboth{\scshape\MakeUppercase{#1}}%
          {\scshape\MakeUppercase{#1}}%
  \pagestyle{\back@pagestyle}
  \vskip 0.5in
}
\newcommand{\afterpostface}{
   \settocdepth{\chapter@tocdepth}%
   \pagestyle{\body@pagestyle}
}
\newcommand{\refname}{References}
\renewcommand{\bibname}{REFERENCES}
\newcommand{\references}{%
  \ifbibpage
    \typeout{*****************     References    ******************}
    \newlinestretch{1.0}
    \if@openright\cleardoublepage\else\clearpage\fi 
    % must clear page here, so that phantomsection\addcontentsline is on the correct page
    \phantomsection%
    \addcontentsline{toc}{chapter}%
      {\texorpdfstring{\Makeuppercase{\refname}}{\refname}}
%% \bibliographystyle{ozu-thesis}
    \bibliography{\@bibfiles}
  \fi
}


%
%% Variations of \cleardoublepage that explicitly set the pagestyle
%% of any inserted blank page.
%
\newcommand{\clearemptydoublepage}%
  {{\pagestyle{empty}\cleardoublepage}}
\newcommand{\clearplaindoublepage}%
  {{\pagestyle{plain}\cleardoublepage}}
\newcommand{\cleartcplaindoublepage}%
  {{\pagestyle{tcplain}\cleardoublepage}}
\newcommand{\clearozuthesisdoublepage}%
  {{\pagestyle{ozuthesis}\cleardoublepage}}

\newcommand{\setfrontpagestyle}[1]{%
  \gdef\front@pagestyle{#1}
}
\newcommand{\setbodypagestyle}[1]{%
  \gdef\body@pagestyle{#1}
}
\newcommand{\setbackpagestyle}[1]{%
  \gdef\back@pagestyle{#1}
}

%%%%%%    Page Styles
%
%% Redefine all four standard page styles (empty, plain, headings,
%% myheadings), based on the definitions in ``report'', so that they
%% conform to the GSO guidelines (and include draft information if
%% applicable).
%%
%% Also, define a new pagestyle ``tcplain'' which is just like ``plain'',
%% but puts page numbers in header (left/right 2page, or right 1page)
%% instead of at the bottom of the page.
%%
%% Then, define a new pagestyle ``ozuthesis''. I like this one better
%% but the Graduate Studies Office doesn't. :-(
%
\renewcommand{\ps@empty}{
  \@tcpagefalse
  \let\@mkboth\@gobbletwo
  \def\@oddfoot{
    \if@draft
      \blDRAFT\hfil
      {\slshape\small\today}\hfil\brDRAFT
    \fi
  }%
  \let\@evenfoot\@oddfoot
  \def\@oddhead{
    \if@draft
      \tlDRAFT\hfil
      {\slshape\small\today}\hfil\trDRAFT
    \fi
  }%
  \let\@evenhead\@oddhead
}%ps@empty

%
%% Pagestyle ``plain''.
%
\renewcommand{\ps@plain}{%
  \@tcpagefalse%
  \let\@mkboth\@gobbletwo%
  \def\@oddfoot{%
    \if@draft\blDRAFT\fi%
    \hfil\thepage\hfil%
    \if@draft\brDRAFT\fi%
  }%
  \let\@evenfoot\@oddfoot%
  \def\@oddhead{%
    \if@draft%
      \tlDRAFT\hfil%
      {\slshape\small\today}\hfil\trDRAFT%
    \fi%
  }%
  \let\@evenhead\@oddhead%
}%ps@plain

%
%% Pagestyle ``headings''.
%
\if@twoside % if two-sided printing
  \renewcommand{\ps@headings}{%
    \@tcpagefalse%
    \let\@mkboth\markboth%
    \def\@oddfoot{%
      \if@draft%
        \blDRAFT\hfil%
        {\slshape\small\today}\hfil\brDRAFT%
      \fi%
    }%
    \let\@evenfoot\@oddfoot%
    \def\@oddhead{%
      \if@draft\tlDRAFT\fi%
      {\slshape\rightmark}\hfil%
      \thepage%
      \if@draft\trDRAFT\fi%
    }%
    \def\@evenhead{%
      \if@draft\tlDRAFT\fi%
      \thepage\hfil%
      {\slshape\leftmark}%
      \if@draft\trDRAFT\fi%
    }%
    \def\chaptermark##1{%
      \markboth
      {\MakeUppercase{%
        \ifnum\c@secnumdepth >\m@ne%
          \@chapapp\ \thechapter. \ %
        \fi ##1}%
      }{}%
    }%
    \def\sectionmark##1{%
      \markright%
      {\MakeUppercase{%
        \ifnum\c@secnumdepth >\z@%
          \thesection. \ %
        \fi ##1}%
      }%
    }%
  }%ps@headings
\else % if one-sided printing
  \renewcommand{\ps@headings}{%
    \@tcpagefalse%
    \let\@mkboth\markboth%
    \def\@oddfoot{%
      \if@draft%
        \blDRAFT\hfil%
        {\slshape\small\today}\hfil\brDRAFT%
      \fi%
    }%
    \def\@oddhead{%
      \if@draft\tlDRAFT\fi%
      {\slshape\rightmark}\hfil%
      \thepage%
      \if@draft\trDRAFT\fi%
    }%
    \def\chaptermark##1{%
      \markright%
      {\MakeUppercase{%
        \ifnum\c@secnumdepth >\m@ne%
          \@chapapp\ \thechapter. \ %
        \fi ##1}%
      }%
    }%
  }%ps@headings
\fi % @twoside

%
%% Pagestyle ``myheadings''.
%
\renewcommand{\ps@myheadings}{%
  \@tcpagefalse%
  \let\@mkboth\@gobbletwo%
  \def\@oddfoot{%
    \if@draft%
      \blDRAFT\hfil%
      {\slshape\small\today}\hfil\brDRAFT%
    \fi%
   }%
   \let\@evenfoot\@oddfoot%
   \def\@oddhead{%
     \if@draft\tlDRAFT\fi%
     {\slshape\rightmark}\hfil%
     \thepage%
     \if@draft\trDRAFT\fi%
   }%
   \def\@evenhead{%
     \if@draft\tlDRAFT\fi%
     \thepage\hfil%
     {\slshape\leftmark}%
     \if@draft\trDRAFT\fi%
   }%
   \let\chaptermark\@gobble\let\sectionmark\@gobble%
}%ps@myheadings

%
%% Pagestyle ``ozuthesis'' (based on ``headings'').
%
\if@twoside % if two-sided printing
  \newcommand{\ps@ozuthesis}{%
    \@tcpagetrue%
    \let\@mkboth\markboth%
    \def\@oddfoot{%
      \if@draft%
        \blDRAFT\hfil%
        {\slshape\small\today}\hfil\brDRAFT%
      \fi%
    }%
    \let\@evenfoot\@oddfoot%
    \def\@oddhead{%
      \if@draft\tlDRAFT\fi%
      {\slshape\rightmark}\hfil%
      \thepage%
      \if@draft\trDRAFT\fi%
    }%
    \def\@evenhead{%
      \if@draft\tlDRAFT\fi%
      \thepage\hfil%
      {\slshape\leftmark}%
      \if@draft\trDRAFT\fi%
    }%
    \def\chaptermark##1{%
      \markboth%
      {\textsc{%
        \ifnum\c@secnumdepth >\m@ne%
          \@chapapp\ \thechapter. \ %
        \fi ##1}%
      }{}%
    }%
    \def\sectionmark##1{%
      \markright%
      {\textsc{%
        \ifnum\c@secnumdepth >\z@%
          \thesection. \ %
        \fi ##1}%
      }
    }%
  }%ps@ozuthesis
\else % if one-sided printing
  \newcommand{\ps@ozuthesis}{%
    \@tcpagetrue%
    \let\@mkboth\markboth%
    \def\@oddfoot{%
      \if@draft%
        \blDRAFT\hfil%
        {\slshape\small\today}\hfil\brDRAFT%
      \fi%
    }%
    \def\@oddhead{%
      \if@draft\tlDRAFT\fi%
      {\slshape\rightmark}\hfil%
      \thepage%
      \if@draft\trDRAFT\fi%
    }%
    \def\chaptermark##1{%
      \markright%
      {\textsc{%
        \ifnum\c@secnumdepth >\m@ne%
          \@chapapp\ \thechapter. \ %
        \fi ##1}%
      }
    }%
  }%ps@ozuthesis
\fi % @twoside

%
%% Pagestyle ``tcplain'' (based on ``plain'').
%
\if@twoside % if two-sided printing
  \newcommand{\ps@tcplain}{%
    \@tcpagetrue%
    \let\@mkboth\markboth%
    \def\@oddfoot{%
      \if@draft%
        \blDRAFT\hfil%
        {\slshape\small\today}\hfil\brDRAFT%
      \fi%
    }%
    \let\@evenfoot\@oddfoot%
    \def\@oddhead{%
      \if@draft\tlDRAFT\fi%
      \hfil\thepage%
      \if@draft\trDRAFT\fi%
    }%
    \def\@evenhead{%
      \if@draft\tlDRAFT\fi%
      \thepage\hfil%
      \if@draft\trDRAFT\fi%
    }%
  }%ps@tcplain
\else % if one-sided printing
  \newcommand{\ps@tcplain}{%
    \@tcpagetrue%
    \let\@mkboth\markboth%
    \def\@oddfoot{%
      \if@draft%
        \blDRAFT\hfil%
        {\slshape\small\today}\hfil\brDRAFT%
      \fi%
    }%
    \def\@oddhead{%
      \if@draft\tlDRAFT\fi%
      \hfil\thepage%
      \if@draft\trDRAFT\fi%
    }%
  }%ps@tcplain
\fi % @twoside


%%%%%%    Document Layout
%
%% Default line spacing: use current setting from options.
%
\linespacing{\@thesislnsp}
%
%% Page layout (see The LaTeX Companion pp.84-86).
%
%% By default, TeX puts the ``reference point'' one inch down and to
%% the right of the top-left corner of the page.  This moves it back
%% to the top-left corner (making the rest of the layout easier to
%% define).
%
\setlength{\voffset}{-1in}
\setlength{\hoffset}{-1in}
%
%% Instead of hard-coding the page layout for letter paper
%% (8.5" x 11"), we will base it on \paperheight and \paperwidth,
%% so that it works with options that change the paper size.
%
\setlength{\textheight}{\paperheight}
\setlength{\textwidth}{\paperwidth}
%
%% Now, set the margin-dependent values.
%
\ifcase\@marginsize % set narrow margins: 1 1/4" left, 3/4" others
%
\addtolength{\textheight}{-1.5in}
\setlength{\topmargin}{.5in}
\setlength{\headsep}{.25in}
\setlength{\footskip}{.25in}
\addtolength{\textwidth}{-2in}
\setlength{\oddsidemargin}{1.25in}
\setlength{\evensidemargin}{.75in}
\setlength{\marginparwidth}{.5in}
\setlength{\marginparsep}{.125in}
%
\or % set normal margins: 1.5 " left, 1" others (modified 01/27/01)
%
\setlength{\textheight}{22cm}
\setlength{\topmargin}{3.5cm}
\setlength{\textwidth}{15cm}
\setlength{\oddsidemargin}{3.5cm}
\setlength{\headsep}{0pt}
\setlength{\footskip}{1.5cm}

%
\or % set wide margins: 1.5" left, 1" others, 2"" top (modified 01/14/00)
%
\addtolength{\textheight}{-3in}
\setlength{\topmargin}{1in}
\setlength{\headsep}{.5in} % reduced by headheight, below
\setlength{\footskip}{0.5in}
\addtolength{\textwidth}{-2.5in}
\setlength{\oddsidemargin}{1.5in}
\setlength{\evensidemargin}{1in}
\setlength{\marginparwidth}{.75in}
\setlength{\marginparsep}{.125in}
%
\or % set extra wide margins: 1 1/2"" all around
%
\addtolength{\textheight}{-3in}
\setlength{\topmargin}{1in}
\setlength{\headsep}{.5in}
\setlength{\footskip}{.5in}
\addtolength{\textwidth}{-3in}
\setlength{\oddsidemargin}{1.5in}
\setlength{\evensidemargin}{1.5in}
\setlength{\marginparwidth}{1in}
\setlength{\marginparsep}{.25in}
%
\or % use oldmargin (OLD GT): 1.5" left and top, 1" others (modified 01/27/01)
%
\addtolength{\textheight}{-2.5in}
\setlength{\topmargin}{0.75in}
\setlength{\headsep}{0.75in}   % reduced by headheight, below
\setlength{\footskip}{0.5in}
\addtolength{\textwidth}{-2.5in}
\setlength{\oddsidemargin}{1.5in}
\setlength{\evensidemargin}{1in}
\setlength{\marginparwidth}{.75in}
\setlength{\marginparsep}{.125in}
%
\fi%@marginsize
%
%% Adjust \headsep to include height of running head.
%
\addtolength{\headsep}{-\headheight}
%
%% Adjust the vertical spacing between the main text and the notes,
%% and between successive notes if they are not single-spaced.
%
\setlength{\skip\footins}{.75\baselineskip}
\if@singlespacednotes
\else
  \let\oldtextsize=\currenttextsize
  \footnotesize
  \setlength{\marginparpush}{\baselineskip}
  \setlength{\footnotesep}{\baselineskip}
  \oldtextsize
\fi % @singlespacednotes
%
%% \flushbottom looks silly with lots of extra space between paragraphs
%% better to put the "extra" space at the bottom of the page!
%
\raggedbottom
%
%% Default page style.
%
\pagestyle{plain}
\setfrontpagestyle{plain}
\setbodypagestyle{plain}
\setbackpagestyle{plain}

%
%% Number subsubsections
%
\setcounter{secnumdepth}{3}

%
%% Show subsubsections in table of contents
%% tocdepth is reset to the value in \setchaptertocdepth
%%   at each \chapter{}, or to the value in \setappendixtocdepth
%%   at each \chapter{} after the \appendix command.  So, if 
%%   you want to change the defaults, use \setchaptertocdepth and 
%%   \setappendixtocdepth.  To temporarily change depth for the 
%%   current section, use a different function: \settocdepth[x].  
%%   You should never need to call \setcounter{tocdepth}{..} 
%%   directly.
%%
%% 0 = chapter only
%% 1 = chapter + sections
%% 2 = chapter, section, subsection
%% 3 = chapter, section, subsection, subsubsection
%
\setcounter{tocdepth}{3} % we call setcounter{tocdepth}{} directly here
                         % but user .tex files should not do this.
% We must insure that the last \setcounter command in the .toc 
% file is NON-ZERO, or the listoffigures and listoftables become 
% empty.  Bad news. Unfortunately, that means we must do some
% raw TeXing here...
%   You would think the \end{postliminary} code would fix this, and it
% does -- but only if you don't \include your vita.  \input{vita} 
% works great because the \end{postliminary} code causes 
% \setcounter{tocdepth}{NONZERO} to be written.  But, if you 
% \include{vita} (or whatever the LAST section before \end{postliminary} 
% is) and the \setcounter command from \end{postliminary} does NOT get 
% written to the .aux file.  Fooey.  This is our workaround.
%   BUT, do NOT remove the one from \end{postliminary}.  When
% \input{vita}, THAT one gets used, and not this one!  Clearly,
% a LaTeX bug.
\AtEndDocument{%
  \immediate\write\@auxout%
  {\string\@writefile{toc}{\string\setcounter{tocdepth}{3}}}
  \clearpage\lastpage@putlabel}%

\setchaptertocdepth{2}
\setappendixtocdepth{0}

%% Disallow page breaks at hyphens (this will give some underfull vbox's,
%% so an alternative is to use \brokenpenalty=100 and manually search
%% for and fix such page breaks)
%
\brokenpenalty=10000

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%TOC Formatting to match MsWord version%%%%%%%%%%%%%%%%
% set the font type to normal
\usepackage[titles,subfigure]{tocloft}
\renewcommand{\cftchapfont}{\normalfont} % Chapters in normal font
\renewcommand{\cftsecfont}{\normalfont}  % Sections in normal font
\renewcommand{\cftsubsecfont}{\normalfont} % Subsections in normal font
\renewcommand{\cftsubsubsecfont}{\normalfont} % Subsections in normal font

\renewcommand{\cftchappagefont}{\normalfont}
\renewcommand{\cftsecpagefont}{\normalfont}
\renewcommand{\cftsubsecpagefont}{\normalfont}
\renewcommand{\cftsubsubsecfont}{\normalfont} % Subsections in normal font

\setlength{\cftbeforechapskip}{10pt} % Adjust chapter line spacing
\setlength{\cftbeforesecskip}{8pt} % Adjust section line spacing
\setlength{\cftbeforesubsecskip}{6pt} % Adjust subsection line spacing


% add prefix to Figure and table lables in LoT and LoF

\renewcommand{\cftfigpagefont}{\bfseries}
\renewcommand{\cfttabpagefont}{\bfseries}
\renewcommand{\cftpartleader}{\cftdotfill{\cftdotsep}} % for parts
\renewcommand{\cftchapleader}{\cftdotfill{\cftdotsep}} % for chapters

\setlength{\cftfigindent}{0pt} % left aligned fig entries
\renewcommand{\cftfigpresnum}{\bfseries Figure }
\renewcommand{\cftfigfont}{\normalfont} % Set table caption font to normal
\renewcommand{\cftfigpagefont}{\normalfont}
\setlength{\cftfignumwidth}{5.5em}
\renewcommand{\cftfigaftersnum}{:}
\renewcommand{\cftdotsep}{1}%
\setlength{\cftbeforefigskip}{10pt} % 10pt space before each table entry

\setlength{\cfttabindent}{0pt} % left aligned tab entries
\renewcommand{\cfttabpresnum}{\bfseries Table }
\renewcommand{\cfttabfont}{\normalfont} % Set table caption font to normal
\renewcommand{\cfttabpagefont}{\normalfont}
\setlength{\cfttabnumwidth}{5em}
\renewcommand{\cfttabaftersnum}{:}
\setlength{\cftbeforetabskip}{10pt} % 10pt space before each table entry

\renewcommand{\cftafterloftitleskip}{10pt} % for list of figures
\renewcommand{\cftafterlottitleskip}{10pt} % for list tables
\renewcommand{\cftaftertoctitleskip}{10pt} % for table of contents

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%