" vim:fdm=marker

" COMMON {{{
" :set guioptions-=m  "remove menu bar
:set guioptions-=T  "remove toolbar
:set guioptions-=r  "remove right-hand scroll bar
:set guioptions-=L  "remove left-hand scroll bar
au GUIEnter * simalt ~x

map <F2> :mksession! ~/vim_session <cr> " Quick write session with F2
map <F3> :source ~/vim_session <cr>     " And load session with F3

set nocompatible
set tabstop=4
set expandtab
set autoindent
" }}

" DISPLAY {{{
set ruler
" set number
set showcmd
set laststatus=2
" }}}

" FONT {{{
set gfn=Consolas:h12:cANSI
" }}}

" COLORS {{{
syntax on
colorscheme koehler
" set t_Co=256
" set background=light
" }}}

" BACKUPS {{{
set nowb
set noswapfile
set nobackup
set viminfo=%100,'100,/100,h,\"500,:100,n~/.viminfo
set history=500
set updatecount=100
" }}}

" SEARCH {{{
set incsearch   " do incremental searching
set ignorecase
set infercase
set hlsearch
set showmatch
set diffopt=filler,iwhite
nnoremap / /\v
vnoremap / /\v
" }}}

" Uncomment the following to have Vim jump to the last position when
" reopening a file
if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif
