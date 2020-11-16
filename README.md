# Programming Resources


## Table of Contents
1. [General](#general)
2. [Project Ideas](#project-ideas)
3. [Project Euler](#project-euler)
4. [Algorithms](#algorithms)
5. [Mazes](#mazes)
6. [Cellular automata](#cellular-automata)
7. [Compilers/interpreters](#compilers/interpreters)
8. [Esoteric programming languages](#esoteric-programming-languages)
9. [Game AI](#game-ai)
10. [Games](#games)
11. [Puzzles](#puzzles)
12. [Fractals and L-systems](#fractals-and-l-systems)
13. [Visual/animation](#visual/animation)
14. [Tiling and packing](#tiling-and-packing)
15. [Physics simulation](#physics-simulation)
16. [Regex](#regex)
17. [Operating Systems](#operating-systems)
18. [Computer Science](#computer-science)
19. [Machine learning](#machine-learning)
20. [AI](#ai)
21. [Cryptography](#cryptography)
22. [Data science](#data-science)
23. [C](#c)
24. [C++](#c++)
25. [JS](#js)
26. [Web development](#web-development)
27. [Python](#python)
28. [PHP](#php)
29. [Java](#java)
30. [Ruby](#ruby)
31. [Perl](#perl)
32. [MIPS](#mips)
33. [ARM](#arm)
34. [Raspberry Pi](#raspberry-pi)
35. [Unix](#unix)
36. [Prolog](#prolog)
37. [Code golf](#code-golf)
38. [Scratch/Snap](#scratch/snap)
39. [Course sites](#course-sites)
40. [Algorithmic challenge sites](#algorithmic-challenge-sites)
41. [Security/CTF sites](#security/ctf-sites)
42. [Competitive coding](#competitive-coding)
43. [Bit twiddling](#bit-twiddling)
44. [Books](#books)
45. [Education](#education)
46. [OMSCS](#omscs)
47. [CCSF](#ccsf)
48. [Jobs](#jobs)
49. [Interview prep](#interview-prep)
50. [Stack Overflow](#stack-overflow)
51. [Fun](#fun)


## General
- <a href="https://www.chessprogramming.org/Keith_Gorlen">Inspiration!</a>
- <a href="https://www.btbytes.com/pl.html">Interesting programming languages</a>
- <a href="http://www.patternlanguage.com/leveltwo/caframe.htm?/leveltwo/../bios/designpatterns.htm">Christopher Alexander's Design Patterns</a>
- <a href="https://en.wikipedia.org/wiki/One-instruction_set_computer">https://en.wikipedia.org/wiki/One-instruction_set_computer</a>


## Project Ideas
- script that calls pd patch, generates artwork and posts to bandcamp via puppeteer or another file sharing service
- write another scrobbler that works by day and follows bandcamp
- bandcamp command line listening streamer based on urls
- Make a simple DIY label CMS or bandcamp clone; host on Heroku
- write some RTS demo sketches
  - <a href="https://sandruski.github.io/RTS-Group-Movement/">https://sandruski.github.io/RTS-Group-Movement/</a>
  - <a href="https://medium.com/@mscansian/a-with-navigation-meshes-246fd9e72424">Nav meshes</a>
  - <a href="http://www.red3d.com/cwr/boids/">Boids</a>
- write a time clock web app and keep exact totals for freelance work
- react native mp3 player with mono mode using mpg123 or something
- auto-queue recent bandcamp releases into command line player via scraping
  - could be a master "to listen" list on glitch which the command line script can automatically pull from. option to search and autoplay something from discogs, youtube or bandcamp
- write a stack machine
- stack overflow comments sentiment analyzer
- do generative eno ambient series covers with pointillist effect in js canvas
- make an IR-\>spim runner in node/mips compiler + host on heroku
- <a href="https://en.wikipedia.org/wiki/Tic-tac-toe_variants">https://en.wikipedia.org/wiki/Tic-tac-toe_variants</a>
- write an app that scrapes recent posts by favorite SO users
- Challenge/project idea lists:
  - <a href="https://www.webfx.com/blog/web-design/10-puzzle-websites-to-sharpen-your-programming-skills/">https://www.webfx.com/blog/web-design/10-puzzle-websites-to-sharpen-your-programming-skills/</a>
  - <a href="https://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/">https://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/</a>
- <a href="http://rosettacode.org/wiki/Rosetta_Code">Look for projects at Rosetta Code</a>
- <a href="https://programmingbydoing.com/">"Programming by Doing" simple projects for students</a>
- Organize mp3s: beets.io and https://www.discogs.com/developers/
- <a href="http://el.media.mit.edu/logo-foundation/index.html">The Logo Foundation</a>
- <a href="https://en.wikipedia.org/wiki/NetLogo">NetLogo</a>
- write a non-acct twitter (or SO) client that can fav and show imgs like birdfeed without having an account.
- write a sandboxed compiler+code runner
- write a winamp plugin that broadcasts now playing to node API on glitch
  - <a href="http://wiki.winamp.com/wiki/Beginner%27s_Basic_Plugin_Guide">http://wiki.winamp.com/wiki/Beginner%27s_Basic_Plugin_Guide</a>
  - <a href="http://forums.winamp.com/showthread.php?t=224914">http://forums.winamp.com/showthread.php?t=224914</a>
- Langs/frameworks/libs to learn: Lisp/Scheme/Ml, Go, rxjs/angular, Rust, COBOL
- <a href="https://developers.google.com/blogger/docs/3.0/getting_started">Listening journal or similar using blogger API</a>
- <a href="https://github.com/TooTallNate/node-lame/blob/master/deps/mpg123/doc/README.remote">make a music player app based on mpg123</a>
  - <a href="https://stackoverflow.com/questions/35781991/run-a-command-that-needs-input-without-hanging-but-still-allow-input">https://stackoverflow.com/questions/35781991/run-a-command-that-needs-input-without-hanging-but-still-allow-input</a>
  - <a href="https://sourceforge.net/p/mpg123/mailman/mpg123-users/thread/CAN5OgQWuYFt4mbbjDZcxMMdTQLZoNiF8AgH5S8Z8rwraN%2B65uA%40mail.gmail.com/">https://sourceforge.net/p/mpg123/mailman/mpg123-users/thread/CAN5OgQWuYFt4mbbjDZcxMMdTQLZoNiF8AgH5S8Z8rwraN%2B65uA%40mail.gmail.com/</a>
  - <a href="https://arstechnica.com/civis/viewtopic.php?f=20&t=850451">https://arstechnica.com/civis/viewtopic.php?f=20&t=850451</a>
- <a href="https://webrtc.github.io/samples/src/content/capture/canvas-video/">Voice/video chat or stream with WebRTC</a>
- Tiger to JS transpiler
- Simple html parser like htm or https://limpet.net/mbrubeck/2014/08/11/toy-layout-engine-2.html
- Google Docs but all vim/markdown. Could add multiplayer multicolor text editor/highlighter. Could be a good edutech project.
- matterjs experiment like https://jsfiddle.net/mityok/c9qt2g28/10/
- make a regex blockly demo on codepen or write a generator for some language that isn't supported yet
- <a href="https://pomb.us/build-your-own-react/">write your own react</a>
- me vs world correspondence chess app for my homepage


## Project Euler
- Next to solve: 189, 244
- <a href="https://www.coin-or.org/PuLP/CaseStudies/a_sudoku_problem.html">#93 Sudoku can also be solved using Integer Linear Programming</a>
- #84 Monopoly is one of the best. Worth solving using both simulation (I used first-class functions) and stochastic matrix (I used numpy). Working out the initial probabilities for the stochastic matrix requires only basic probability, but it's tricky.
- <a href="http://www.geeksforgeeks.org/eulers-totient-function/">Euler's totient function</a>


## Algorithms
- <a href="https://algs4.cs.princeton.edu/home/">Princeton Algorithms</a>
- <a href="http://cslibrary.stanford.edu/">Stanford CS Education Library</a>
- <a href="https://inst.eecs.berkeley.edu/~cs61b/fa17/materials/lectures/">Berkeley CS61B lectures</a>
- <a href="http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html">Yale CPSC 223</a>
- <a href="https://www.algorithm-archive.org/">Algorithm archive</a>
- <a href="https://en.wikipedia.org/wiki/Skip_list">Skip list</a>
- <a href="https://en.wikipedia.org/wiki/Splay_tree">Splay tree</a>
- <a href="https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/">Word ladder</a>
- <a href="https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/">Disjoint set/ union find</a>
- <a href="https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/">Segment trees</a>
- <a href="https://en.wikipedia.org/wiki/Self-avoiding_walk">Self-avoiding walk</a>
- <a href="https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm">Bellman-Ford</a>
- <a href="http://www.cs.princeton.edu/courses/archive/spr10/cos226/assignments.html">Princeton algorithm assignments</a>
- <a href="https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html">Boyer-Moore majority vote algorithm</a>
- <a href="https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes">Sieve of Eratosthenes</a>
- <a href="https://en.wikipedia.org/wiki/Fermat%27s_factorization_method">Fermat's factorization method</a>
- <a href="http://andreinc.net/2010/12/11/euclids-algorithm-reducing-fraction-to-lowest-terms/">Euclid's algorithm</a>
- <a href="https://en.wikipedia.org/wiki/Karatsuba_algorithm">Karatsuba algorithm</a>
- <a href="http://codereview.stackexchange.com/questions/66450/simplify-a-fraction">Simplify a fraction</a>
- <a href="http://blog.jamisbuck.org/">Basil & Fabian</a>
- <a href="https://developmentality.wordpress.com/tag/car-talk/">Car talk puzzlers</a>
- <a href="https://towardsdatascience.com/solve-slide-puzzle-with-hill-climbing-search-algorithm-d7fb93321325">Sliding puzzle solving with hill climbing</a>
- <a href="https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf">Dancing Links</a>
- <a href="https://en.wikipedia.org/wiki/K-way_merge_algorithm">k-way merge algorithm</a>
- <a href="https://en.wikipedia.org/wiki/DPLL_algorithm">DPLL</a>

### DP
- <a href="https://runestone.academy/runestone/books/published/pythonds/Recursion/DynamicProgramming.html">Coin change</a>
- <a href="https://en.wikipedia.org/wiki/Maximum_subarray_problem">Maximum subarray problem (Kadane's algorithm)</a>
- <a href="https://people.cs.clemson.edu/~bcdean/dp_practice/">Box stacking problem (and other DP problems)</a>
- <a href="https://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/">DP text justify</a>
- <a href="http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/">DP coin change</a>
- <a href="https://www.youtube.com/watch?v=ocZMDMZwhCY">MIT open courseware DP lecture</a>
- <a href="https://people.eecs.berkeley.edu/~vazirani/algorithms/chap6.pdf">Algs/DP</a>
- The "correct change" problem looks like it's equivalent to the "subset sum" problem, which is a special case of the knapsack problem. Wikipedia says these are all NP, but efficiency can be improved by dynamic programming. That's why I'm thinking a transposition table may help.
- <a href="http://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number">Sum numbers in a list</a>
- <a href="https://en.wikipedia.org/wiki/Knapsack_problem">Knapsack problem</a>
- PE #136, #173, and #174

### Graphs
- <a href="https://cstheory.stackexchange.com/questions/11855/how-do-the-state-of-the-art-pathfinding-algorithms-for-changing-graphs-d-d-l">Pathfinding algorithm comparison</a>
- <a href="https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/">Shortest path algorithms</a>
- <a href="https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/">MST</a>
- <a href="http://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm">Floyd Warshall algorithm</a>
- <a href="https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm">Dijkstra's algorithm</a>

### Trees
- <a href="https://algs4.cs.princeton.edu/33balanced/">Balanced search trees</a>
- <a href="http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/">Tree traversal construction</a>
- <a href="https://www.youtube.com/watch?v=H13iz0rbeeo">Determine if a tree is a BST</a>
- <a href="https://en.wikipedia.org/wiki/Left-child_right-sibling_binary_tree">https://en.wikipedia.org/wiki/Left-child_right-sibling_binary_tree</a>
- <a href="https://en.wikipedia.org/wiki/AVL_tree">https://en.wikipedia.org/wiki/AVL_tree</a>

### Strings/arrays
- <a href="http://stackoverflow.com/questions/24720332/c-find-all-possible-combinations-of-a-string-in-another-string">Find combinations of a string in another string</a>
- <a href="https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm">Knuth-Morris-Pratt</a>
- Rabin-Karp


## Mazes
- <a href="http://www.astrolog.org/labyrnth/algrithm.htm">Think Labyrinth</a>
- <a href="http://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap">Buckblog maze generation algorithm overview</a>
- <a href="https://en.wikipedia.org/wiki/Random_walk">Random walk</a>


## Cellular automata
- <a href="https://en.wikipedia.org/wiki/Cellular_automaton">Cellular automaton</a>
- <a href="https://en.wikipedia.org/wiki/Elementary_cellular_automaton">Elementary cellular automaton</a>
- <a href="https://en.wikipedia.org/wiki/Rule_30">Rule 30</a>
- <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Conway's game of life</a>
- <a href="https://en.wikipedia.org/wiki/Turmite">Turmite</a>
- <a href="https://www.wolframscience.com/nks/p65--more-cellular-automata/">Wolfram cellular automata</a>
- <a href="http://natureofcode.com/book/chapter-7-cellular-automata/">Nature of Code by Shiffman, chapter 7</a>
- <a href="https://en.wikipedia.org/wiki/Wireworld">Wireworld</a>
- <a href="https://en.wikipedia.org/wiki/Brian%27s_Brain">Brian's Brain</a>
- <a href="https://en.wikipedia.org/wiki/Von_Neumann_cellular_automaton">Von Neumann</a>
- <a href="https://en.wikipedia.org/wiki/Langton%27s_loops">Langton's loops</a>
- <a href="https://en.wikipedia.org/wiki/CoDi">CoDi</a>
- <a href="https://en.wikipedia.org/wiki/Life-like_cellular_automaton">Life-like cellular automata (incl. Seeds)</a>
- <a href="http://math.hws.edu/eck/js/edge-of-chaos/CA-info.html">Interactive CA and other sundry JS animations</a>


## Compilers/interpreters
- Write a Forth interpreter:
  - <a href="https://www.forth.com/starting-forth/9-forth-execution/">Forth lang tutorial</a>
  - <a href="http://openbookproject.net/py4fun/forth/forth.html">Python Forth interpreter</a>
  - <a href="https://skilldrick.github.io/easyforth/">Easy Forth tutorial</a>
- Stanford compilers courses:
  - <a href="http://web.stanford.edu/class/archive/cs/cs143/cs143.1128/">http://web.stanford.edu/class/archive/cs/cs143/cs143.1128/</a>
  - <a href="https://lagunita.stanford.edu/courses/Engineering/Compilers/Fall2014/about">https://lagunita.stanford.edu/courses/Engineering/Compilers/Fall2014/about</a>
- <a href="https://classroom.udacity.com/courses/cs262">Udacity programming languages course</a>
- <a href="https://ruslanspivak.com/lsbasi-part1/">Let's build a simple interpreter</a>
- <a href="https://github.com/NeilFraser/JS-Interpreter">JS interpreter in JS (good for sandboxing)</a>
- <a href="http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf">Incremental approach to compiler construction</a>
- <a href="https://norasandler.com/2017/11/29/Write-a-Compiler.html">Write a compiler</a>
- <a href="http://craftinginterpreters.com/">Crafting Interpreters</a>
- <a href="http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html">Python interpreter in Python</a>
- <a href="https://nearley.js.org/docs/grammar">nearley/moo js</a>
- <a href="https://dickgrune.com/">Compiler books</a>
- <a href="https://jack-vanlightly.com/blog/2016/2/3/creating-a-simple-tokenizer-lexer-in-c">Create a simple tokenizer in C#</a>
- <a href="https://gnuu.org/2009/09/18/writing-your-own-toy-compiler/">Writing your own toy compiler</a>
- <a href="https://en.wikibooks.org/wiki/Compiler_Construction/Lexical_analysis">Lexical analysis</a>
- <a href="https://blog.mgechev.com/2017/09/16/developing-simple-interpreter-transpiler-compiler-tutorial/#references">Simple tutorial and useful references</a>
- <a href="http://effbot.org/zone/simple-top-down-parsing.htm">Simple top-down parsing</a>
- My first language front-end:
  - <a href="https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html">https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html</a>
  - <a href="https://github.com/llvm-mirror/llvm/blob/master/examples/Kaleidoscope/MCJIT/initial/toy.cpp">https://github.com/llvm-mirror/llvm/blob/master/examples/Kaleidoscope/MCJIT/initial/toy.cpp</a>
- <a href="https://stackoverflow.com/questions/1669/learning-to-write-a-compiler">Mega compilers resource</a>
- <a href="https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/">CS143</a>
- <a href="https://www.seas.upenn.edu/~cis341/current/">CIS341</a>
- <a href="https://concatenative.org/wiki/view/Concatenative%20language">Concatenative Languages</a>
- <a href="https://tiarkrompf.github.io/notes/?/just-write-the-parser/">https://tiarkrompf.github.io/notes/?/just-write-the-parser/</a>
- lispcompiler.com
- <a href="https://compilers.iecc.com/crenshaw/">Let's Build a Compiler, by Jack Crenshaw</a>
- <a href="https://twitter.com/munificentbob/status/901543375945388032">Nystrom's compiler books</a>


## Esoteric programming languages
- <a href="http://catseye.tc/">Cat's Eye</a>
- <a href="https://esolangs.org/wiki/Main_Page">Esolangs.org</a>
- <a href="https://en.wikipedia.org/wiki/Esoteric_programming_language">Esoteric programming languages</a>
- <a href="http://www.frox25.no-ip.org/~mtve/code/eso/bef/chess/">Chess in befunge</a>


## Game AI
- <a href="http://webdocs.cs.ualberta.ca/~jonathan/PREVIOUS/Courses/657/Notes/10.Single-agentSearch.pdf">IDDFS/single agent search</a>
- <a href="https://algorithmsinsight.wordpress.com/graph-theory-2/ida-star-algorithm-in-general/">IDA*</a>
- <a href="https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/">A* n puzzle</a>
- <a href="https://en.wikipedia.org/wiki/Jump_point_search">A* Jump-point search optimization</a>
- <a href="https://www.cc.gatech.edu/~surban6/2019fa-gameAI/lectures/2019_08_28_searchMovement_continued2-presented%20in%20class.pdf">Navmesh</a>
- <a href="https://www.codeproject.com/Articles/37024/Simple-AI-for-the-Game-of-Breakthrough">Breakthrough AI tutorial</a>
- <a href="https://en.wikipedia.org/wiki/SSS*">SSS*</a>
- Monte Carlo Tree Search:
  - <a href="https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/">https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/</a>
  - <a href="http://www.baeldung.com/java-monte-carlo-tree-search">http://www.baeldung.com/java-monte-carlo-tree-search</a>
  - <a href="https://introcs.cs.princeton.edu/java/98simulation/">https://introcs.cs.princeton.edu/java/98simulation/</a>
  - <a href="https://www.coursera.org/lecture/c-plus-plus-b/4-2-monte-carlo-a3Z4u">https://www.coursera.org/lecture/c-plus-plus-b/4-2-monte-carlo-a3Z4u</a>
- <a href="https://en.wikipedia.org/wiki/Principal_variation_search">Principal variation search</a>
- <a href="https://en.wikipedia.org/wiki/MTD-f">MTD-f</a>
- <a href="https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search">Iterative deepening DFS</a>
- <a href="https://en.wikipedia.org/wiki/Iterative_deepening_A*">Iterative deepening A*</a>
- <a href="https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning">Alpha-beta pruning</a>
- <a href="http://cwoebker.com/posts/tic-tac-toe">Tic tac toe AI</a>
- Minimax:
  - <a href="https://www.neverstopbuilding.com/blog/minimax">https://www.neverstopbuilding.com/blog/minimax</a>
  - <a href="https://www.leaseweb.com/labs/2013/12/python-tictactoe-tk-minimax-ai/">https://www.leaseweb.com/labs/2013/12/python-tictactoe-tk-minimax-ai/</a>
- <a href="https://en.wikipedia.org/wiki/Negamax">Negamax</a>
- <a href="https://inventwithpython.com/invent4thed/chapter15.html">Othello basic</a>
- <a href="http://inventwithpython.com/pygame/chapter10.html">4 grid games from Al Sweigart</a>
- <a href="https://www.youtube.com/watch?v=_1NzUMWeU4c">Game of the Amazons</a>


## Games
- <a href="https://en.wikipedia.org/wiki/List_of_puzzle_video_games">List of puzzle video games</a>
- <a href="https://en.wikipedia.org/wiki/Tile-matching_video_game">Tile-matching video games</a>
- <a href="https://en.wikipedia.org/wiki/Microsoft_Entertainment_Pack">Microsoft Entertainment Pack</a>
- <a href="https://en.wikipedia.org/wiki/Mahjong_solitaire">Mahjong solitaire</a>
- 2d visibility:
  - <a href="https://www.redblobgames.com/articles/visibility/">https://www.redblobgames.com/articles/visibility/</a>
  - <a href="http://journal.stuffwithstuff.com/2015/09/07/what-the-hero-sees/">http://journal.stuffwithstuff.com/2015/09/07/what-the-hero-sees/</a>
  - <a href="https://legends2k.github.io/2d-fov/design.html">https://legends2k.github.io/2d-fov/design.html</a>
  - <a href="https://www.emanueleferonato.com/2015/02/03/play-with-light-and-dark-using-ray-casting-and-visibility-polygons/">In Phaser using a raycasting lib</a>
- <a href="https://dev.opera.com/articles/3d-games-with-canvas-and-raycasting-part-1/">3d Wolfenstein raycasting tutorial in JS</a>
- <a href="https://en.wikipedia.org/wiki/Minichess">Minichess</a>
- <a href="https://www.redblobgames.com/grids/hexagons/">Minesweeper with hex grid (try tri grid as well)</a>
- <a href="https://www.youtube.com/watch?v=KboGyIilP6k">Dots and boxes</a>
- <a href="https://en.wikipedia.org/wiki/Breakthru_(board_game)">Breakthru</a>
- <a href="https://en.wikipedia.org/wiki/Beast_(video_game)">Beast</a>
- <a href="http://programarcadegames.com/">Program arcade games</a>
- <a href="http://www.atariarchives.org/basicgames/">BASIC games</a>
- <a href="https://en.wikipedia.org/wiki/Nim">Nim</a>
- <a href="http://www.instructables.com/id/Peg-Game-IQ-Test-Solution/">Emily's pegs game</a>
- <a href="https://www.youtube.com/watch?v=1t782B0zK3Y">Fire & Ice</a>
- <a href="https://www.youtube.com/watch?v=WV-rQfYKSGA">Filler/Qualio</a>
  - <a href="https://stackoverflow.com/questions/59692024">Generating levels</a>
- Tower defense
- <a href="https://en.wikipedia.org/wiki/Hexapawn">Hexapawn</a>
- Octopawn
- <a href="https://en.wikipedia.org/wiki/Pipe_Mania">Pipe Dream</a>
- <a href="https://boardgamegeek.com/boardgame/681/quarto">Quarto</a>
- <a href="https://en.wikipedia.org/wiki/Mancala">Mancala</a>
- <a href="https://en.wikipedia.org/wiki/JezzBall">Jezzball</a>
- Freerice clone
- <a href="https://en.wikipedia.org/wiki/Patience_(game)">Patience</a>
- <a href="https://en.wikipedia.org/wiki/Hex_(board_game)">Hex</a>
- <a href="https://dke.maastrichtuniversity.nl/m.winands/loa/">Lines of action</a>
- <a href="https://en.wikipedia.org/wiki/Boulder_Dash">Boulder Dash</a>
- <a href="https://en.wikipedia.org/wiki/Tic-tac-toe_variants">Ultimate tic tac toe or other variants</a>
- <a href="https://en.wikipedia.org/wiki/Marble_Madness">Marble Madness</a>
- <a href="https://en.wikipedia.org/wiki/Loco-Motion_(video_game)">Loco-Motion</a>
- <a href="https://en.wikipedia.org/wiki/Digger_(video_game)">Digger</a>
- <a href="https://en.wikipedia.org/wiki/Nine_Men%27s_Morris">Nine Men's Morris</a>
- <a href="https://en.wikipedia.org/wiki/Rummikub">Rummikub</a>
- Hnefatafl
- Hive
- Go
- 2048
- Boggle
- Lemmings
- Snake: 2 player versions, add obstacles, snake tetris, ai
  - <a href="https://johnflux.com/2015/05/02/nokia-6110-part-3-algorithms/">https://johnflux.com/2015/05/02/nokia-6110-part-3-algorithms/</a>
  - <a href="https://towardsdatascience.com/slitherin-solving-the-classic-game-of-snake-with-ai-part-3-genetic-evolution-33186e6be110">https://towardsdatascience.com/slitherin-solving-the-classic-game-of-snake-with-ai-part-3-genetic-evolution-33186e6be110</a>
- <a href="https://en.wikipedia.org/wiki/Solved_game">Solved games list</a>
- <a href="https://en.wikipedia.org/wiki/Mastermind_(board_game)">Mastermind</a>
- <a href="https://osgameclones.com/">Open souce game clones</a>
- <a href="https://en.wikipedia.org/wiki/List_of_abstract_strategy_games">List of abstract strategy games</a>
- <a href="http://inventwithpython.com/chapter15.html">Reversi</a>
- Checkers, misere checkers and variants:
  - <a href="https://boardgamegeek.com/geeklist/147417/best-checkers-variants">https://boardgamegeek.com/geeklist/147417/best-checkers-variants</a>
  - <a href="http://www.di.fc.ul.pt/~jpn/gv/checkers.htm">http://www.di.fc.ul.pt/~jpn/gv/checkers.htm</a>
  - <a href="https://en.wikipedia.org/wiki/Draughts#Invented_variants">https://en.wikipedia.org/wiki/Draughts#Invented_variants</a>
- ASCII games:
  - <a href="http://ifarchive.org/">http://ifarchive.org/</a>
  - <a href="http://www.8bs.com/othrdnld/manuals/publications.shtml">http://www.8bs.com/othrdnld/manuals/publications.shtml</a>
  - <a href="https://en.wikipedia.org/wiki/Jotto">https://en.wikipedia.org/wiki/Jotto</a>
  - <a href="https://en.wikipedia.org/wiki/NetHack">https://en.wikipedia.org/wiki/NetHack</a>
  - <a href="http://www.iancgbell.clara.net/elite/text/index.htm">http://www.iancgbell.clara.net/elite/text/index.htm</a>
  - MUDS such as God Wars
- Interactive fiction:
  - <a href="http://literateprogramming.com/adventure.pdf">Knuth adventure</a>
  - <a href="https://www.tads.org/">TADS3</a>
- <a href="https://www.youtube.com/watch?v=txUvD5_ROIU">Tile-based game tutorial</a>
- Puzzlescript:
  - <a href="https://puzzlescriptgallery.tumblr.com/">Tumblr</a>
  - <a href="https://itch.io/games/made-with-puzzlescript">Itch</a>


## Puzzles
- <a href="https://en.wikipedia.org/wiki/Category:Logic_puzzles">Logic puzzles list (KenKen, Sudoku, Sokoban, etc)</a>
- <a href="https://www.chiark.greenend.org.uk/~sgtatham/puzzles/">Simon Tatham</a>
- Do chess packing puzzles
- <a href="http://www2.stetson.edu/~efriedma/">Erich Friendman's Puzzle Palace</a>
- <a href="https://en.wikipedia.org/wiki/Slitherlink">Slitherlink</a>
- <a href="http://www.mindsports.nl/index.php/puzzle-links">Mindsports (links resource)</a>
- <a href="http://garethrees.org/2007/06/10/zendoku-generation/#section-4">Zendoku puzzle generation</a>
- <a href="https://en.wikipedia.org/wiki/Sudoku_solving_algorithms">Sudoku solving algorithms</a>
- <a href="https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions">Generating sudoku boards</a>
- <a href="https://www.youtube.com/watch?v=49KvZrioFB0">Mondrian puzzle</a>
- <a href="http://nikoli.co.jp/en/puzzles/">Various puzzles from the Sudoku inventors</a>
- <a href="http://norvig.com/sudoku.html">Peter Norvig on Sudoku and other constraint problems (such as the skyscraper puzzle)</a>
- <a href="https://www.wikihow.com/Solve-a-Magnets-Puzzle">More constraint puzzles</a>
- <a href="https://en.wikipedia.org/wiki/Nonogram">Nonogram</a>
- <a href="https://en.wikipedia.org/wiki/Ricochet_Robot">Ricochet Robots</a>
- <a href="https://en.wikipedia.org/wiki/Slothouber%E2%80%93Graatsma_puzzle">Slothouber-Graatsma puzzle</a>
- <a href="https://en.wikipedia.org/wiki/Packing_problems">Packing</a>
- <a href="https://www.youtube.com/watch?v=hW4nB-ZAhts">Triomino packing</a>
- <a href="https://www.youtube.com/watch?v=i_TU49MioEE">Irregular hexagon packing</a>
- <a href="https://en.wikipedia.org/wiki/Mathematical_puzzle">Mathematical puzzle</a>
- <a href="https://en.wikipedia.org/wiki/Soma_cube">Soma cube</a>
- <a href="https://www.youtube.com/channel/UCEPZPgtnTvj2F3qTCLfaP4w">Assorted logic games</a>
- <a href="https://en.wikipedia.org/wiki/Lights_Out_(game)">Lights Out</a>
- <a href="http://www.puzzle-bridges.com/">A bunch of puzzle games</a>
- <a href="https://en.wikipedia.org/wiki/Dissection_puzzle">Dissection puzzle</a>
  - <a href="https://www.youtube.com/watch?v=P-9qBV-9Fos">https://www.youtube.com/watch?v=P-9qBV-9Fos</a>
- <a href="https://en.wikipedia.org/wiki/Tangram">Tangram</a>
- <a href="http://www.bricks-game.de/">Klotski gone insane (Bricks game)</a>
- TopSpin and other puzzles:
  - <a href="https://www.jaapsch.net/puzzles/topspin.htm">https://www.jaapsch.net/puzzles/topspin.htm</a>
  - <a href="https://www.jaapsch.net/">https://www.jaapsch.net/</a>


## Fractals and L-systems
- <a href="http://algorithmicbotany.org/">Algorithmic Botany</a>
- <a href="https://www.youtube.com/watch?v=kKT0v3qhIQY&index=20&list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH">Space colonization</a>
- <a href="http://paulbourke.net/fractals/">Paul Bourke</a>
- <a href="http://www.playingwithchaos.net/">Book on JS fractals</a>
- <a href="http://paulbourke.net/fractals/lsys/">L-systems user notes/manual</a>
- <a href="https://10klsystems.wordpress.com/examples/">L-system examples</a>
- <a href="http://mathforum.org/advanced/robertd/lsys2d.html">2d L-systems</a>
- <a href="http://fiys169.blogspot.com/2015/11/the-harriss-spiral.html">Harriss spiral</a>
- <a href="http://www.kevs3d.co.uk/dev/lsystems/">Full-featured L-systems app</a>
- <a href="https://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension">Hausdorff fractals list</a>
- <a href="https://en.wikipedia.org/wiki/Abelian_sandpile_model">Abelian sandpiles</a>
- <a href="https://en.wikipedia.org/wiki/Koch_snowflake">Koch snowflake</a>
- <a href="https://en.wikipedia.org/wiki/Sierpinski_carpet">Sierpinski carpet</a>
- <a href="http://mathworld.wolfram.com/HafermanCarpet.html">Haferman Carpet</a>
- <a href="https://en.wikipedia.org/wiki/Rose_(mathematics)">Rose</a>
- <a href="https://en.wikipedia.org/wiki/Chaos_game">Chaos game</a>
- <a href="https://en.wikipedia.org/wiki/Barnsley_fern">Barnsley Fern</a>


## Visual/animation
- <a href="http://zreference.com/projects/graphics/">Inspiring zreference projects</a>
- <a href="https://bit101.github.io/lab/dailies/170413.html">Also inspiring, bit101 dailies</a>
- <a href="http://cs.brown.edu/people/rtamassi/gdhandbook/">Handbook of Graph Drawing and Visualization</a>
- Convex hull:
  - <a href="https://en.wikipedia.org/wiki/Convex_hull_algorithms">https://en.wikipedia.org/wiki/Convex_hull_algorithms</a>
  - <a href="https://en.wikipedia.org/wiki/Orthogonal_convex_hull">https://en.wikipedia.org/wiki/Orthogonal_convex_hull</a>
- Delaunay triangulation:
  - <a href="https://transcendentcode.wordpress.com/2014/01/26/triangulation/">https://transcendentcode.wordpress.com/2014/01/26/triangulation/</a>
  - <a href="https://en.wikipedia.org/wiki/Delaunay_triangulation">https://en.wikipedia.org/wiki/Delaunay_triangulation</a>
  - <a href="http://www.geom.uiuc.edu/~samuelp/del_project.html#algorithms">http://www.geom.uiuc.edu/~samuelp/del_project.html#algorithms</a>
  - <a href="https://en.wikipedia.org/wiki/Voronoi_diagram#Algorithms">https://en.wikipedia.org/wiki/Voronoi_diagram#Algorithms</a>
- <a href="https://en.wikipedia.org/wiki/Graph_drawing">Graph drawing</a>
- Isometric:
  - <a href="https://stackoverflow.com/questions/892811/drawing-isometric-game-worlds">https://stackoverflow.com/questions/892811/drawing-isometric-game-worlds</a>
  - <a href="http://www.gamedesign.jp/flash/slidingblock/slidingblock.html">http://www.gamedesign.jp/flash/slidingblock/slidingblock.html</a>
- <a href="http://goto80.com/chipflip/06/">goto80 ASCII art</a>
- <a href="https://en.wikipedia.org/wiki/Fibonacci_number">Fibonacci spiral</a>
- <a href="https://s-media-cache-ak0.pinimg.com/564x/d6/ff/64/d6ff6450173c6410c919b06e07958227.jpg">Architecture: look for triangle perspective designs, Escher</a>
- Do a visual plotting the orthocenter, medicenter, and circumcenter of a triangle
- Write a script that turns text into blocky ASCII text or renders images in ASCII
- <a href="https://jsxgraph.uni-bayreuth.de/wiki/index.php/Category:Examples">JSXGraph</a>
- Bezier Curves:
  - <a href="https://pomax.github.io/bezierinfo/">A Primer on Bezier Curves</a>
  - <a href="http://www.victoriakirst.com/beziertool/">Bezier curve tool</a>
  - Chaining Bezier curves:
    - <a href="http://html5tutorial.com/how-to-join-two-bezier-curves-with-the-canvas-api/">http://html5tutorial.com/how-to-join-two-bezier-curves-with-the-canvas-api/</a>
    - <a href="http://www.algosome.com/articles/continuous-bezier-curve-line.html">http://www.algosome.com/articles/continuous-bezier-curve-line.html</a>
    - <a href="https://stackoverflow.com/questions/12295773/joining-two-b%C3%A9zier-curves-smoothly-c2-continuous">https://stackoverflow.com/questions/12295773/joining-two-b%C3%A9zier-curves-smoothly-c2-continuous</a>
    - <a href="https://www.cl.cam.ac.uk/teaching/2000/AGraphHCI/SMEG/node3.html">https://www.cl.cam.ac.uk/teaching/2000/AGraphHCI/SMEG/node3.html</a>
    - <a href="https://en.wikipedia.org/wiki/Composite_B%C3%A9zier_curve">https://en.wikipedia.org/wiki/Composite_B%C3%A9zier_curve</a>
    - <a href="https://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/Bezier/bezier-der.html">https://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/Bezier/bezier-der.html</a>
- <a href="https://www.ibiblio.org/e-notes/Splines/Intro.htm">Splines intro</a>
- <a href="http://arc.id.au/CanvasLayers.html">Canvas stack</a>
- <a href="https://stackoverflow.com/questions/10486084/generate-animated-gif-with-html5-canvas">Create gif from a canvas animation</a>
- Animate the Collatz Conjecture
- <a href="https://mepler.com/The-ReCode-Project">ReCode Project (computer art repository)</a>
- <a href="http://dada.compart-bremen.de">CompArt</a>
- <a href="http://algorists.org/algorist.html">The Algorists</a>
- <a href="https://en.wikipedia.org/wiki/Sol_LeWitt">Sol LeWitt</a>
- <a href="https://js.do/samples/sombrero">3d sombrero and other algorithms</a>
- <a href="https://necessarydisorder.wordpress.com/2017/11/15/drawing-from-noise-and-then-making-animated-loopy-gifs-from-there/">Necessary Disorder</a>
- <a href="https://threejsfundamentals.org/">ThreeJS fundamentals</a>
- <a href="http://mrdoob.com/">Mr. Doob three.js collection</a>


### WebGL
- <a href="https://thebookofshaders.com/">The book of shaders</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial">WebGL tutorial</a>
- <a href="https://bits.coop/articles/rigging-and-animation/">Try out regl</a>
- <a href="https://github.com/regl-project/regl">https://github.com/regl-project/regl</a>
- <a href="https://github.com/regl-project/awesome-regl">https://github.com/regl-project/awesome-regl</a>
- <a href="http://regl.party/api">http://regl.party/api</a>
- <a href="https://github.com/Erkaman">Erkaman</a>
- <a href="https://vallandingham.me/regl_intro.html">An Intro to regl for Data Visualization</a>


## Tiling and packing
- <a href="https://en.wikipedia.org/wiki/Lubachevsky%E2%80%93Stillinger_algorithm">Lubachevsky packing algorithm</a>
- <a href="https://en.wikipedia.org/wiki/Rhombille_tiling">Rhombile tiling</a>
- <a href="https://en.wikipedia.org/wiki/Tangram">Tangrams</a>
- <a href="https://en.wikipedia.org/wiki/Tiling_puzzle">Tiling puzzle</a>
- <a href="https://thebrickinthesky.wordpress.com/2013/03/17/l-systems-and-penrose-p3-in-inkscape">L-systems in inkscape</a>
- <a href="https://en.wikipedia.org/wiki/Girih_tiles">Girih tiles</a>
- <a href="https://en.wikipedia.org/wiki/Wallpaper_group">Wallpaper group</a>
- <a href="https://morphingtiling.wordpress.com/page/2/">Morphing Tiling</a>
- <a href="https://transcendentcode.wordpress.com/">Transcendent Code</a>
- Penrose tiling:
  - <a href="http://preshing.com/20110831/penrose-tiling-explained/">http://preshing.com/20110831/penrose-tiling-explained/</a>
  - <a href="http://www.math.ubc.ca/~cass/courses/m308-02b/projects/schweber/penrose.html">http://www.math.ubc.ca/~cass/courses/m308-02b/projects/schweber/penrose.html</a>
- <a href="https://en.wikipedia.org/wiki/Substitution_tiling">Substitution tiling</a>
- <a href="http://jsfiddle.net/a4ZbG/">"Isometic" JS example</a>
- <a href="https://en.wikipedia.org/wiki/Truncated_hexagonal_tiling#Triakis_triangular_tiling">Triaki's</a>
- <a href="https://en.wikipedia.org/wiki/Litema">Litema</a>
- <a href="https://en.wikipedia.org/wiki/Kuba_textiles">Kuba textiles</a>
- <a href="https://www.jasondavies.com/">Jason Davies</a>
- <a href="https://www.flickr.com/photos/quasimondo/albums/72157624374940604">Circle packing flickr</a>


## Physics simulation
- <a href="https://en.wikipedia.org/wiki/Falling-sand_game">Falling sand game</a>
- <a href="https://andrew.wang-hoyer.com/experiments/cloth/">Cloth physics</a>
- <a href="https://www.youtube.com/watch?v=3HjO_RGIjCU">Verlet integration</a>
- <a href="https://en.wikipedia.org/wiki/Ragdoll_physics">Ragdoll physics</a>
- <a href="https://www.youtube.com/watch?v=11ZmRlR7sOQ">Coding math tutorial</a>
- <a href="https://www.khanacademy.org/computing/computer-programming/programming-natural-simulations/programming-vectors/p/project-computational-creatures">Khan Academy natural simulations course</a>
- Double pendulum:
  - <a href="https://www.youtube.com/watch?v=uWzPe_S-RVE&t=0s&list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH&index=131">Coding challenge 93</a>
  - <a href="https://en.wikipedia.org/wiki/Double_pendulum">https://en.wikipedia.org/wiki/Double_pendulum</a>
  - <a href="https://www.youtube.com/watch?v=neh86u7_TIk">https://www.youtube.com/watch?v=neh86u7_TIk</a>
- <a href="http://proquest.safaribooksonline.com/9781787123663">Game physics cookbook</a>
- <a href="https://en.wikipedia.org/wiki/Jansen%27s_linkage">Jansen's linkage</a>
- <a href="https://leanpub.com/natureincode">Nature in Code book</a>
- Sin & cos:
  - <a href="https://inventwithpython.com/blog/2012/07/18/using-trigonometry-to-animate-bounces-draw-clocks-and-point-cannons-at-a-target/">Brief intro to sin & cos</a>
  - <a href="http://www.helixsoft.nl/articles/circle/sincos.htm">and another intro to sin & cos with some mode 7 content</a>
- <a href="https://circles-bouncing-off-lines.glitch.me/docs/circles-bouncing-off-lines.html">Circles bouncing off lines tutorial</a>
- <a href="https://maryrosecook.com/">Mary Rose Cook</a>
- <a href="http://harry.me/blog/2011/02/17/neat-algorithms-flocking/">Flocking behaviors</a>
- <a href="https://www.youtube.com/playlist?list=PLW3Zl3wyJwWOpdhYedlD-yCB7WQoHf-My">Math for game developers</a>
- <a href="https://www.redblobgames.com/pathfinding/a-star/introduction.html">Variety of pathfinding tutorials</a>
- <a href="http://cowboyprogramming.com/2007/01/05/blob-physics/">Blobs</a>
- <a href="https://2dengine.com/?p=tutorials">Various tutorials for 2d graphics (isometric, polygon, collision, platformers, networking, etc)</a>
- <a href="https://www.ibm.com/developerworks/library/wa-build2dphysicsengine/">Simple 2d physics engine</a>
- <a href="http://hugobdesigner.blogspot.com/">2d physics engine 3 part tutorial</a>
- <a href="https://www.gamasutra.com/view/feature/131424/pool_hall_lessons_fast_accurate_.php?print=1">Pool hall physics</a>
- Collision detection:
  - <a href="http://www.dyn4j.org/2010/01/sat/">http://www.dyn4j.org/2010/01/sat/</a>
  - <a href="https://gamedevelopment.tutsplus.com/tutorials/collision-detection-using-the-separating-axis-theorem--gamedev-169">https://gamedevelopment.tutsplus.com/tutorials/collision-detection-using-the-separating-axis-theorem--gamedev-169</a>
  - <a href="https://wildbunny.co.uk/blog/2011/04/20/collision-detection-for-dummies/">https://wildbunny.co.uk/blog/2011/04/20/collision-detection-for-dummies/</a>
  - <a href="https://www.codeproject.com/Articles/15573/2D-Polygon-Collision-Detection">https://www.codeproject.com/Articles/15573/2D-Polygon-Collision-Detection</a>
  - <a href="https://stackoverflow.com/questions/10962379/how-to-check-intersection-between-2-rotated-rectangles/12414951#12414951">https://stackoverflow.com/questions/10962379/how-to-check-intersection-between-2-rotated-rectangles/12414951#12414951</a>
  - <a href="https://github.com/antishow/collision-demo/tree/master/library/js/src">https://github.com/antishow/collision-demo/tree/master/library/js/src</a>
  - <a href="http://paulbourke.net/fractals/randomtile/">http://paulbourke.net/fractals/randomtile/</a>
  - <a href="https://maryrosecook.com/blog/post/how-to-do-2d-collision-detection">https://maryrosecook.com/blog/post/how-to-do-2d-collision-detection</a>
  - <a href="http://www.metanetsoftware.com/technique/tutorialA.html">http://www.metanetsoftware.com/technique/tutorialA.html</a>
  - <a href="http://www.migapro.com/circle-and-rotated-rectangle-collision-detection/">http://www.migapro.com/circle-and-rotated-rectangle-collision-detection/</a>
  - <a href="https://gist.github.com/eliasdaler/502b54fcf1b515bcc50360ce874e81bc">https://gist.github.com/eliasdaler/502b54fcf1b515bcc50360ce874e81bc</a>
  - <a href="https://gist.github.com/cwleonard/e124d63238bda7a3cbfa">https://gist.github.com/cwleonard/e124d63238bda7a3cbfa</a>
  - <a href="https://gist.github.com/LindseyB/394536">https://gist.github.com/LindseyB/394536</a>
  - <a href="https://gist.github.com/enghqii/5af2512ced10849016e635fcf2d15d29">https://gist.github.com/enghqii/5af2512ced10849016e635fcf2d15d29</a>
  - <a href="https://github.com/tetoblivion/Collision_response_with_rotation/blob/master/respondToCollision.cpp">https://github.com/tetoblivion/Collision_response_with_rotation/blob/master/respondToCollision.cpp</a>
  - <a href="https://gamedev.stackexchange.com/questions/32611/what-is-the-best-way-to-handle-simultaneous-collisions-in-a-physics-engine">https://gamedev.stackexchange.com/questions/32611/what-is-the-best-way-to-handle-simultaneous-collisions-in-a-physics-engine</a>
- Quadtrees:
  - <a href="https://en.wikipedia.org/wiki/Quadtree">https://en.wikipedia.org/wiki/Quadtree</a>
  - <a href="https://gamedevelopment.tutsplus.com/tutorials/quick-tip-use-quadtrees-to-detect-likely-collisions-in-2d-space--gamedev-374">https://gamedevelopment.tutsplus.com/tutorials/quick-tip-use-quadtrees-to-detect-likely-collisions-in-2d-space--gamedev-374</a>


## Regex
- <a href="https://www.regular-expressions.info/refadv.html">Advanced regex features ref sheet</a>
- <a href="http://www.cs.sun.ac.za/~abvdm/regex.html">Regex Static Analysis</a>
- <a href="https://www.regular-expressions.info/catastrophic.html">Catastrophic Backtracking</a>
- <a href="https://swtch.com/~rsc/regexp/">Implementing Regular Expressions</a>
- <a href="https://rcoh.me/posts/no-magic-regular-expressions/">Write a regex engine</a>
- <a href="https://learning.tarokuriyama.com/2020/02/mini-regex.html">Mini regex</a>
- <a href="https://www.regular-expressions.info/replaceconditional.html">Replace with conditional</a>
- <a href="http://nikic.github.io/2012/06/15/The-true-power-of-regular-expressions.html">True power of regex</a>


## Operating Systems
- <a href="https://www.cc.gatech.edu/classes/AY2010/cs4210_fall/">CS4210 archive</a>
- <a href="https://www2.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/">Operating Systems notes</a>
- <a href="https://cs.nyu.edu/~mwalfish/classes/ut/s11-cs372h/hw/sol8.html">OS @ NYU</a>
- <a href="https://cs162.eecs.berkeley.edu/">Berkeley CS162</a>
- <a href="https://akkadia.org/drepper/cpumemory.pdf">What every programmer should know about memory</a>
- <a href="https://greenteapress.com/wp/semaphores/">The Little Book of Semaphores</a>
- <a href="https://csapp.cs.cmu.edu/">Computer Systems: A Programmer's Perspective</a>


## Computer Science
- <a href="https://cs.meta.stackexchange.com/questions/599/reference-answers-to-frequently-asked-questions/847#847">CS SE FAQ</a>
- <a href="http://www.cs.toronto.edu/~hehner/best.html">Rick Hehner's top 10</a>
- <a href="https://softwarefoundations.cis.upenn.edu/">Software foundations book series</a>
- <a href="http://www.jflap.org/">JFLAP</a>
- <a href="https://yurichev.com/writings/SAT_SMT_by_example.pdf">SAT SMT by Example</a>


## Machine learning
- <a href="http://www.deeplearningbook.org/">Deep Learning book</a>
- <a href="https://github.com/wasd12345">wasd12345 on GitHub</a>


## AI
- <a href="http://ai.berkeley.edu/project_overview.html">Berkeley CS188 AI with Pacman</a>
- <a href="https://www.cs.rit.edu/~rlc/Courses/IS/">Intro to Intelligent Systems</a>


## Cryptography
- <a href="https://crypto.stanford.edu/~dabo/cryptobook/BonehShoup_0_4.pdf">A Graduate Course in Applied Cryptography</a>
- <a href="http://security.stackexchange.com/questions/45963/diffie-hellman-key-exchange-in-plain-english">DH key exchange in plain English</a>


## Data science
- APIs/Datasets
  - <a href="https://github.com/toddmotto/public-apis">https://github.com/toddmotto/public-apis</a>
  - <a href="https://github.com/public-apis/public-apis/blob/master/README.md">https://github.com/public-apis/public-apis/blob/master/README.md</a>
  - <a href="https://apilist.fun/">https://apilist.fun/</a>
  - <a href="https://www.quora.com/What-are-some-cool-fun-random-APIs-such-as-BreweryDB">https://www.quora.com/What-are-some-cool-fun-random-APIs-such-as-BreweryDB</a>
  - <a href="https://botwiki.org/resources/datasets/">https://botwiki.org/resources/datasets/</a>
  - <a href="https://botwiki.org/resources/apis/">https://botwiki.org/resources/apis/</a>
  - <a href="https://randomuser.me/api/?results=100">https://randomuser.me/api/?results=100</a>
  - <a href="https://github.com/MuseumofModernArt/exhibitions">unsplash photo API</a>
  - <a href="http://makeup-api.herokuapp.com/">makeup</a>
  - <a href="https://diatoms.org/species">diatoms</a>
  - <a href="https://github.com/awesomedata/awesome-public-datasets">https://github.com/awesomedata/awesome-public-datasets</a>
  - <a href="https://github.com/mwaskom/seaborn-data">https://github.com/mwaskom/seaborn-data</a>
  - <a href="https://vincentarelbundock.github.io/Rdatasets/datasets.html">R datasets</a>
  - <a href="https://catalog.data.gov/dataset?tags=plants">data.gov</a>
  - CIA world factbook:
    - <a href="https://github.com/thewiremonkey/factbook.csv">https://github.com/thewiremonkey/factbook.csv</a>
    - <a href="https://www.cia.gov/library/publications/the-world-factbook/">https://www.cia.gov/library/publications/the-world-factbook/</a>
  - <a href="https://github.com/erikgahner/PolData/blob/master/PolData.csv">https://github.com/erikgahner/PolData/blob/master/PolData.csv</a>
  - <a href="https://github.com/jldbc/gunsandcrime">https://github.com/jldbc/gunsandcrime</a>
  - <a href="https://gist.github.com/klmr/23ed79f973c75b11b0b5">https://gist.github.com/klmr/23ed79f973c75b11b0b5</a>
  - <a href="https://www.washingtonpost.com/wp-srv/health/interactives/guns/ownership.html">https://www.washingtonpost.com/wp-srv/health/interactives/guns/ownership.html</a>
  - <a href="https://restcountries.eu/">https://restcountries.eu/</a>
  - <a href="https://rel.ink/">https://rel.ink/</a>
  - <a href="https://pipedream.com/">https://pipedream.com/</a>
  - <a href="https://example-data.draftbit.com/">https://example-data.draftbit.com/</a>
  - <a href="https://github.com/vera-institute/incarceration_trends">https://github.com/vera-institute/incarceration_trends</a>
- Inspirational projects:
  - <a href="https://douweosinga.com/projects/">https://douweosinga.com/projects/</a>


## C
- <a href="http://www.buildyourownlisp.com/">Build your own lisp</a>
- <a href="https://wiki.osdev.org/Tutorials">Write your own OS</a>
- <a href="https://beej.us/guide/bggdb/">Beej guide to GDB</a>
- <a href="https://barrgroup.com/Embedded-Systems/Books/Embedded-C-Coding-Standard">C coding standard</a>
- <a href="http://www.seebs.net/faqs/c-iaq.html">C IAQ</a>


## C++
- C++ SFML for games and graphics
- <a href="https://solarianprogrammer.com/2012/10/17/cpp-11-async-tutorial/">Async C++ tutorial</a>


## JS
- <a href="https://www.dwitter.net/">Dwitter (140 chars or less JS code)</a>
- <a href="https://javascript30.com/">30 day vanilla JS challenge</a>


## Web development
- Jekyll blog:
  - <a href="https://www.youtube.com/watch?v=xdxfyFS3pog">https://www.youtube.com/watch?v=xdxfyFS3pog</a>
  - <a href="https://jekyllrb.com/docs/installation/">https://jekyllrb.com/docs/installation/</a>
- <a href="https://www.bitballoon.com">Bitballoon for hosting web apps</a>
- Jamstack/netlify/gridsome

### CSS
- <a href="https://css-tricks.com/snippets/css/complete-guide-grid/">Grid</a>
- <a href="https://codepen.io/rachelandrew/pens/public">Rachel Andrew (CSS grid examples)</a>
- <a href="https://davidwalsh.name/css-cube">CSS cube</a>


## Python
- <a href="http://norvig.com/lispy.html">Write a Lisp interpreter in Python</a>
- <a href="https://www.pythonanywhere.com/">Host a free Python web app</a>
- <a href="http://www.nltk.org/book/">Natural language processing with Python</a>
- <a href="http://inventwithpython.com/pygame/">Pygame</a>
- <a href="https://automatetheboringstuff.com/">Automate the boring stuff</a>
- <a href="https://www.rose-hulman.edu/Users/faculty/young/CS-Classes/resources/Python/ZelleGraphics.html">Simple Python graphics library</a>
- Flask:
  - <a href="https://exploreflask.com/en/latest/">https://exploreflask.com/en/latest/</a>
  - <a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world">https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world</a>
  - <a href="http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/">http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/</a>
- Python data structures & algorithms
  - <a href="http://interactivepython.org/runestone/static/pythonds/index.html">http://interactivepython.org/runestone/static/pythonds/index.html</a>
  - <a href="http://www.brpreiss.com/books/opus7/">http://www.brpreiss.com/books/opus7/</a>
- <a href="http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf">Computer vision with python</a>
- <a href="http://www.effectivepython.com/">Effective Python</a>
- <a href="http://interactivepython.org/courselib/static/thinkcspy/index.html">How to think like a computer scientist</a>
- <a href="http://pythonchallenge.com/">Python Challenge</a>
- <a href="http://effbot.org/tkinterbook/">Tkinterbook</a>


## PHP
- Sessions/logins:
  - <a href="http://culttt.com/2013/02/04/how-to-save-php-sessions-to-a-database/">http://culttt.com/2013/02/04/how-to-save-php-sessions-to-a-database/</a>
  - <a href="http://shiflett.org/articles/storing-sessions-in-a-database">http://shiflett.org/articles/storing-sessions-in-a-database</a>
  - <a href="http://php.net/manual/en/function.session-set-save-handler.php">http://php.net/manual/en/function.session-set-save-handler.php</a>
  - <a href="https://www.sitepoint.com/writing-custom-session-handlers/">https://www.sitepoint.com/writing-custom-session-handlers/</a>
  - <a href="https://github.com/sprain/PHP-MySQL-Session-Handler/blob/master/MySqlSessionHandler.php">https://github.com/sprain/PHP-MySQL-Session-Handler/blob/master/MySqlSessionHandler.php</a>
  - <a href="https://github.com/JamieCressey/PHP-MySQL-Session-Handler">https://github.com/JamieCressey/PHP-MySQL-Session-Handler</a>
  - <a href="https://github.com/kahwee/php-db-session-handler">https://github.com/kahwee/php-db-session-handler</a>
  - <a href="https://www.allphptricks.com/simple-user-registration-login-script-in-php-and-mysqli/">https://www.allphptricks.com/simple-user-registration-login-script-in-php-and-mysqli/</a>
  - <a href="https://phpeasystep.com/workshopview.php?id=6">https://phpeasystep.com/workshopview.php?id=6</a>
  - <a href="http://www.eggslab.net/php-login-script/">http://www.eggslab.net/php-login-script/</a>
  - <a href="http://codewithawa.com/posts/admin-and-user-login-in-php-and-mysql-database">http://codewithawa.com/posts/admin-and-user-login-in-php-and-mysql-database</a>
  - <a href="https://www.formget.com/login-form-in-php/">https://www.formget.com/login-form-in-php/</a>
- <a href="https://www.ibm.com/developerworks/library/os-php-gamescripts1/">PHP game scripts</a>
- <a href="https://phppot.com/php/simple-php-chat-using-websocket/">Websocket chat</a>
- <a href="http://phpsadness.com/">PHP Sadness</a>
- <a href="https://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/">More PHP Sadness</a>


## Java
- <a href="https://google.github.io/styleguide/javaguide.html">Google style guide</a>
- <a href="https://struts.apache.org/">Good Java web framework for learning generics</a>
- <a href="http://java2novice.com/java-sorting-algorithms/">Java sorting algorithms</a>
- <a href="http://stackoverflow.com/questions/2793150/using-java-net-urlconnection-to-fire-and-handle-http-requests">Java send HTTP request</a>
- <a href="http://stackoverflow.com/questions/3649014/send-email-using-java">Java send email</a>


## Ruby
- <a href="http://poignant.guide/book/chapter-6.html">Why's Poignant Guide to Ruby</a>
- <a href="http://ruby-doc.com/docs/ProgrammingRuby/html/tut_stdtypes.html">Nice Ruby regex tutorial</a>
- <a href="http://ruby-doc.com/docs/ProgrammingRuby/html/rubyworld.html">Programming Ruby</a>


## Perl
- <a href="http://perldoc.perl.org/perldsc.html">Perl data structures cookbook</a>


## MIPS
- <a href="http://students.cs.tamu.edu/tanzir/csce350/reference/syscalls.html">MIPS system calls</a>
- <a href="https://uweb.engr.arizona.edu/~ece369/Resources/spim/QtSPIM_examples.pdf">Learning MIPS and SPIM</a>
- <a href="https://courses.engr.illinois.edu/cs232/sp2012/section/disc2sol.pdf">recursion</a>
- <a href="https://courses.cs.washington.edu/courses/cse378/09wi/lectures/lec05.pdf">https://courses.cs.washington.edu/courses/cse378/09wi/lectures/lec05.pdf</a>
- <a href="https://courses.cs.washington.edu/courses/cse378/07au/lectures/L4.pdf">https://courses.cs.washington.edu/courses/cse378/07au/lectures/L4.pdf</a>
- <a href="https://courses.cs.washington.edu/courses/cse410/09sp/examples/MIPSCallingConventionsSummary.pdf">https://courses.cs.washington.edu/courses/cse410/09sp/examples/MIPSCallingConventionsSummary.pdf</a>
- <a href="https://en.wikibooks.org/wiki/MIPS_Assembly/Control_Flow_Instructions">https://en.wikibooks.org/wiki/MIPS_Assembly/Control_Flow_Instructions</a>
- <a href="https://www.coursehero.com/file/45823007/cs311-03-isa-Ipdf/">https://www.coursehero.com/file/45823007/cs311-03-isa-Ipdf/</a>
- <a href="https://github.com/kyungyunlee/CS311-Computer-Organization/tree/master/project2/Project2">https://github.com/kyungyunlee/CS311-Computer-Organization/tree/master/project2/Project2</a>
- <a href="https://github.com/mightydeveloper/MIPS-Assembler">https://github.com/mightydeveloper/MIPS-Assembler</a>
- <a href="https://www.youtube.com/watch?v=z3ltaJ5UU5I">https://www.youtube.com/watch?v=z3ltaJ5UU5I</a>
- <a href="https://learnxinyminutes.com/docs/mips/">https://learnxinyminutes.com/docs/mips/</a>
- <a href="https://chortle.ccsu.edu/AssemblyTutorial/index.html">https://chortle.ccsu.edu/AssemblyTutorial/index.html</a>
- <a href="http://www.cs.uwm.edu/classes/cs315/Bacon/Lecture/HTML/ch05s03.html">http://www.cs.uwm.edu/classes/cs315/Bacon/Lecture/HTML/ch05s03.html</a>
- <a href="http://homepage.divms.uiowa.edu/~ghosh/1-28-10.pdf">http://homepage.divms.uiowa.edu/~ghosh/1-28-10.pdf</a>
- <a href="http://cgi.cse.unsw.edu.au/~cs1521/17s2/docs/spim.php">http://cgi.cse.unsw.edu.au/~cs1521/17s2/docs/spim.php</a>
- <a href="https://www.dsi.unive.it/~gasparetto/materials/MIPS_Instruction_Set.pdf">https://www.dsi.unive.it/~gasparetto/materials/MIPS_Instruction_Set.pdf</a>
- <a href="https://www.doc.ic.ac.uk/lab/secondyear/spim/node9.html">https://www.doc.ic.ac.uk/lab/secondyear/spim/node9.html</a>
- <a href="https://www.doc.ic.ac.uk/lab/secondyear/spim/node20.html">https://www.doc.ic.ac.uk/lab/secondyear/spim/node20.html</a>
- <a href="https://www.math.unipd.it/~sperduti/ARCH09/mips_assembler.pdf">https://www.math.unipd.it/~sperduti/ARCH09/mips_assembler.pdf</a>
- <a href="http://www.mrc.uidaho.edu/mrc/people/jff/digital/MIPSir.html">http://www.mrc.uidaho.edu/mrc/people/jff/digital/MIPSir.html</a>


## ARM
- Thinkingeek Raspberry Pi Asssembler:
  - <a href="https://thinkingeek.com/2013/01/09/arm-assembler-raspberry-pi-chapter-1/">Site</a>
  - <a href="https://personal.utdallas.edu/~pervin/RPiA/RPiA.pdf">eBook</a>
- <a href="http://www.microdigitaled.com/ARM/ASM_ARM/Software/ARM_Assembly_Programming_Using_Raspberry_Pi_GUI.pdf">ARM Assembly Using Raspberry PI</a>
- <a href="http://www.science.smith.edu/dftwiki/index.php/Tutorial:_Assembly_Language_with_the_Raspberry_Pi">Smith College ARM Tutorial</a>
- <a href="http://www.bravegnu.org/gnu-eprog/hello-arm.html">Hello ARM</a>
- Tutorials:
  - <a href="https://www.youtube.com/watch?v=5HILZon7pVE">https://www.youtube.com/watch?v=5HILZon7pVE</a>
  - <a href="https://www.youtube.com/watch?v=zl04ZfdkiuM">https://www.youtube.com/watch?v=zl04ZfdkiuM</a>
  - <a href="https://www.youtube.com/watch?v=1VAcZr2wQzo">https://www.youtube.com/watch?v=1VAcZr2wQzo</a>


## Raspberry Pi
- Extending the life of the SD card:
  - <a href="https://domoticproject.com/extending-life-raspberry-pi-sd-card/">https://domoticproject.com/extending-life-raspberry-pi-sd-card/</a>
  - <a href="https://raspberrypi.stackexchange.com/questions/169/how-can-i-extend-the-life-of-my-sd-card">https://raspberrypi.stackexchange.com/questions/169/how-can-i-extend-the-life-of-my-sd-card</a>


## Unix
- <a href="http://overthewire.org/wargames/bandit/">Bandit wargames</a>
- <a href="http://learnvimscriptthehardway.stevelosh.com/">Learn vim script</a>


## Prolog
- <a href="http://cs.union.edu/~striegnk/courses/nlp-with-prolog/html/node5.html#l1.prolog">FSAs in Prolog</a>
- <a href="https://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/">99 prolog problems</a>


## Code golf
- <a href="https://code-golf.io/">code-golf.io</a>
- <a href="https://js1k.com/">js1k</a>
- <a href="https://js1024.fun/">https://js1024.fun/</a>
- <a href="http://golf.shinh.org/">anarchy golf</a>
- <a href="http://terje2.frox25.no-ip.org/perlgolf_history_070109.pdf">Perlgolf history</a>


## Scratch/Snap
- <a href="https://forkphorus.github.io/">Forkphorus</a>
- <a href="https://sulfurous.aau.at/">Sulfurous</a>
- Useful Scratch reference topics:
  - <a href="https://wiki.scratch.mit.edu/wiki/Array#Multidimensional_Arrays_in_Scratch">https://wiki.scratch.mit.edu/wiki/Array#Multidimensional_Arrays_in_Scratch</a>
  - <a href="https://wiki.scratch.mit.edu/wiki/List_of_Mathematical_Functions_Done_in_Scratch">https://wiki.scratch.mit.edu/wiki/List_of_Mathematical_Functions_Done_in_Scratch</a>
  - <a href="https://wiki.scratch.mit.edu/wiki/Recursion_and_Fractals#Creating_the_Koch_Curve">https://wiki.scratch.mit.edu/wiki/Recursion_and_Fractals#Creating_the_Koch_Curve</a>
- <a href="http://www.ocsmag.com/2016/07/12/dump-scratch-use-blockly-or-snap-instead/">Snap instead of Scratch</a>
- <a href="http://www.multiwingspan.co.uk/scratch.php?page=ex1">Multiwingspan projects</a>


## Course sites
- <a href="http://codingthematrix.com/">Coding the Matrix (linear algebra through CS)</a>
- <a href="http://nand2tetris.org/">Nand2Tetris</a>
- <a href="https://www.udemy.com/the-advanced-web-developer-bootcamp/">Advanced Web Developer Bootcamp</a>
- <a href="https://www.lynda.com/portal/patron?org=sfpl.org">Lynda SFPL</a>
- <a href="https://www.coursera.org/learn/algorithms-part1">Coursera algorithms classes (pts 1 & 2)</a>
- <a href="https://egghead.io/">Egghead</a>
- <a href="https://www.udacity.com/course/intro-to-theoretical-computer-science--cs313">Udacity intro to theoretical CS</a>
- <a href="http://jeffe.cs.illinois.edu/teaching/algorithms/">Jeff Erickson's algorithms</a>
- <a href="https://courses.cs.washington.edu/courses/cse326/03wi/326lecturesa.shtml">UW Data Structures & Algorithms</a>
- Math:
  - <a href="https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/">MIT OCW Math for CS</a>
  - <a href="https://www.math.fsu.edu/~pkirby/mad2104/SlideShow/CourseNotesMAD2104.pdf">FSU Discreet Math I</a>
  - <a href="http://www-math.mit.edu/~djk/calculus_beginners/">Calculus for beginners</a>
  - <a href="https://www.calculusexpert.com/library/">https://www.calculusexpert.com/library/</a>
  - <a href="http://www.mathmeetsyou.com/home/trigonometry">http://www.mathmeetsyou.com/home/trigonometry</a>
  - <a href="http://www.greenteapress.com/thinkbayes/html/index.html">http://www.greenteapress.com/thinkbayes/html/index.html</a>
  - <a href="https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/">https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/</a>


## Algorithmic challenge sites
- <a href="https://code.google.com/codejam/past-contests">Google Code Jam</a>
  - <a href="https://www.go-hero.net/jam/16/">Go-Hero</a> has archive all the past Google Code Jam problems w/ solutions
- <a href="https://www.reddit.com/r/dailyprogrammer/">Daily Programmer</a>
- <a href="https://www.mathworks.com/matlabcentral/cody/problems">Math problems</a>
- <a href="https://www.learneroo.com/">Learneroo</a>
- <a href="https://www.topcoder.com/getting-started">Topcoder</a>
- <a href="https://www.hackerearth.com/challenges/">Hacker Earth</a>
- <a href="https://www.codechef.com/">Code chef</a>
- <a href="http://www.spoj.com/">SPOJ</a>
- <a href="http://www.exercism.io">Exercism</a>
  - <a href="https://www.youtube.com/watch?v=neXJOhHj8ik&index=6&list=PLyGLemjnH3ukTGW8TYCzdu7jQe0U-wEKi">Talk on exercism</a>
- <a href="https://kattis.com">Kattis</a>
- <a href="http://codingbat.com">Coding Bat</a>
- <a href="https://acm.timus.ru/">Timus</a>
- <a href="http://codekata.pragprog.com/">Code kata</a>
- <a href="https://www.root-me.org/en/Challenges/Web-Client/Javascript-Native-code">Root me</a>


## Security/CTF sites
- <a href="https://picoctf.com/">Hacking competition for kids</a>
- <a href="https://hackthissite.org/">https://hackthissite.org/</a>
- <a href="https://www.hackthebox.eu/">https://www.hackthebox.eu/</a>


## Competitive coding
- <a href="https://cses.fi/">CSES</a>
- <a href="https://cses.fi/book/book.pdf">Competitive Programmer's Handbook</a>
- <a href="http://web.stanford.edu/class/cs97si/">Introduction to programming contests</a>
- <a href="http://codeforces.com/">Codeforces</a>
- <a href="https://www.topcoder.com/community/competitive-programming/">Topcoder</a>
- <a href="http://www.pvv.ntnu.no/~spaans/programming.html">Tons of tips & links</a>
- <a href="https://swerc.eu/2017/problems/">SWERC past problem sets</a>


## Bit twiddling
- <a href="http://graphics.stanford.edu/~seander/bithacks.html">http://graphics.stanford.edu/~seander/bithacks.html</a>
- <a href="http://realtimecollisiondetection.net/blog/?p=78">http://realtimecollisiondetection.net/blog/?p=78</a>


## Books
- <a href="https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list">Definitive C++ book list</a>
- <a href="http://proquest.safaribooksonline.com/">Tons of free CS books</a>
- <a href="http://www.greenteapress.com/thinkbayes/html/index.html">Think Bayes/DSP/Complexity/OS/etc</a>
- <a href="https://www.fuzzingbook.org/">Fuzzing book (software testing)</a>
- "Book of Proof" Hammack
- <a href="http://discrete.openmathbooks.org/dmoi3.html">Discrete Math</a>
- <a href="http://www.finseth.com/craft/index.html">Craft of Text Editors</a>


## Education
- SFSU
  - <a href="http://bulletin.sfsu.edu/colleges/science-engineering/computer-science/ms-computer-science/">http://bulletin.sfsu.edu/colleges/science-engineering/computer-science/ms-computer-science/</a>
  - Prospective students are welcome to send any questions to the graduate advising assistant at (csgrad@sfsu.edu)
- <a href="http://www.vtmit.vt.edu/">VT</a>
- <a href="http://getcoding.hackreactor.com/remote-part-time">Bootcamps</a>
- Internships:
  - <a href="https://www.indeed.com/q-Software-Engineering-Intern-l-San-Francisco-Bay-Area,-CA-jobs.html">https://www.indeed.com/q-Software-Engineering-Intern-l-San-Francisco-Bay-Area,-CA-jobs.html</a>
  - <a href="http://www.engineerjobs.com/internships/software-engineering/california/bay-area.php">http://www.engineerjobs.com/internships/software-engineering/california/bay-area.php</a>
  - <a href="https://www.smartrecruiters.com/Line2/112808690-web-developer-internship-front-end">https://www.smartrecruiters.com/Line2/112808690-web-developer-internship-front-end</a>
- <a href="https://www.mills.edu/academics/graduate-programs/computer-science/">Mills</a>
- <a href="https://www.calstateonline.net/Cal-State-Campuses/CSU-Fullerton">CSU Fullerton</a>
- <a href="https://www.ces.sdsu.edu/science-computers-technology/advanced-certificate-web-and-mobile-applications-development">Adv. certif. in web/mobile via SDSU</a>
- <a href="http://www.northeastern.edu/siliconvalley/admissions/">Northeastern Silicon Valley</a>
- <a href="https://www.collegechoice.net/rankings/best-online-masters-in-computer-science/">College choice CS</a>
- <a href="https://www.recurse.com/">Recurse non-bootcamp</a>


## OMSCS

- <a href="https://drive.google.com/drive/u/0/folders/1ELjIQBaekmSF0fspJn4W7iuOWh3UxYN_">Course syllabi</a>
- <a href="https://omscs.gatech.edu/search/node/course%20videos">Course videos</a>
- **Remember to convert EST to PST for registration**

### Courses to take
- <a href="https://www-users.cs.umn.edu/~karypis/parbook/">CSE 6220 Intro to High Performance Computing</a>
- CS 6265 Information Security Lab
  - <a href="https://tc.gts3.org/cs6265/2020-spring/cal.html">https://tc.gts3.org/cs6265/2020-spring/cal.html</a>
  - <a href="http://phrack.com">http://phrack.com</a>
- CS 6035 Intro to Information Security
  - <a href="https://drive.google.com/file/d/19XxlM2Mo4wBonnQdVnUUo10Cqix-Odej/view">https://drive.google.com/file/d/19XxlM2Mo4wBonnQdVnUUo10Cqix-Odej/view</a>
- CS 6250 Computer Networks
  - <a href="https://www.cc.gatech.edu/~rama/CS2200-External/">prereq course</a>
  - <a href="https://github.com/ossu/computer-science/issues/520">more prereq/alternate suggestions</a>
- ISYE 6501 Intro to Analytics Modeling
  - <a href="http://faculty.marshall.usc.edu/gareth-james/ISL/">http://faculty.marshall.usc.edu/gareth-james/ISL/</a>
- CS 6260 Applied Cryptography
  - <a href="https://teapowered.dev/assets/crypto-notes.pdf">https://teapowered.dev/assets/crypto-notes.pdf</a>
- CS 7280 Network Science
- ISYE 6644 Simulation
- CS 6601 Artificial Intelligence
- CS 6460 Educational Technology
- <a href="https://www.reddit.com/r/OMSCS/comments/a445mn/can_you_recommend_textbooks_for_the_cs_6300_6310/">interesting 6310 textbooks worth looking into</a>

### Completed courses
- Fall 18: CS 6200 Intro to Operating Systems
- Spring 19: CS 6210 Advanced Operating Systems
- Summer 19: CS 6340 Software Analysis and Test
  - <a href="https://cs.au.dk/~amoeller/spa/">Static Program Analysis (main text)</a>
  - <a href="https://d1b10bmlvqabco.cloudfront.net/attach/jbe3aw2nwc031n/ixory6sosP2/jcigv7z03w61/books.pdf">Relevant books</a>
  - <a href="http://rightingcode.org/">Course website</a>
  - <a href="https://classroom.udacity.com/courses/cs259">Nice follow-up Udacity course</a>
- Fall 19: CS 6290 High Performance Computer Architecture
- Spring 20: CS 8803-O08 Compilers
- Spring 20: CS 6291 Embedded Systems Optimization
- Summer 20: CS 7638 AI for Robotics
  - <a href="https://teapowered.dev/assets/ai4r-notes.pdf">https://teapowered.dev/assets/ai4r-notes.pdf</a>
- Fall 20: ECE 8843 Side channels and their role in cybersecurity
- Spring 21:
  - CS 6515 Graduate Algorithms
    - <a href="https://gt-algorithms.com/">https://gt-algorithms.com/</a>
    - <a href="https://cs170.org/">https://cs170.org/</a>
    - <a href="http://omscs.wikidot.com/courses:cs6515">http://omscs.wikidot.com/courses:cs6515</a>
    - <a href="https://teapowered.dev/assets/ga-notes.pdf">https://teapowered.dev/assets/ga-notes.pdf</a>
    - <a href="http://timroughgarden.org/">http://timroughgarden.org/</a>
  - CS 7210 Distributed Systems
    - <a href="https://drive.google.com/file/d/1m9h2xvSLKXpopMBrfUbIkNa9apiKkOHC/view">https://drive.google.com/file/d/1m9h2xvSLKXpopMBrfUbIkNa9apiKkOHC/view</a>


## CCSF
- <a href="https://github.com/CCSF-Coders/learning-resources">CCSF Coders resources page</a>
- <a href="https://sites.google.com/site/koalalearn/fa2011/cs211s">CS211s notes</a>

### CCSF courses to take
- CS   177   Software Engineering
- CS   231   Advanced Python Programming
- CS   211D  Android Programming
- CS   211E  Advanced Java: Enterprise Edition
- CS   150P  SQL Server T-SQL Programming
- CS   155B  MySQL Database Administration
- CS   260A  Linux System Administration
- CS   260P  Linux Administration Projects
- CS   197P  Technical Interview Prep
- CS   197V  Version Control & Code Repos
- CS   199   Independent Study
- CS   256   Data Visualization
- CNIT 141   Cryptography For Computer Networks
- CNIT 123   Ethical Hacking
- CNIT 124   Adv. Ethical Hacking
- CNIT 127   Exploit Development
- MATH  80   Probability and Statistics
- MATH  95   Trigonometry
- MATH 110A  Calculus I
- MATH 115   Discrete Mathematics
- MATH 120   Linear Algebra

### CCSF courses taken
- CS   270   Comp Architecture w/ Assembly
  - <a href="https://fog.ccsf.edu/~gboyd/cs270/online/index.html">https://fog.ccsf.edu/~gboyd/cs270/online/index.html</a>
  - <a href="https://fog.ccsf.edu/~gboyd/cs270/HowThisCourseWorks.pdf">https://fog.ccsf.edu/~gboyd/cs270/HowThisCourseWorks.pdf</a>

### CCSF certificates I've attained:
  - <a href="https://www.ccsf.edu/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerScience/ComputerProgrammingJavaCertificate.pdf">Java</a>
  - <a href="http://www.ccsf.edu/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerScience/WebApplicationProgrammingCertificate.pdf">Web application programming</a>
  - <a href="https://www.ccsf.edu/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerScience/ComputingSkillsforScientistsCertificate.pdf">Computing skills for scientists</a>
  - <a href="http://www.ccsf.edu/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerNetworkingandInformationTechnology/JavaScriptSpecialistCertificate.pdf">JS specialist</a>
  - <a href="http://www.ccsf.edu/content/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerNetworkingandInformationTechnology/WebSiteDevelopmentTechniquesCertificate.pdf">Web site development techniques</a>
  - <a href="http://www.ccsf.edu/content/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerNetworkingandInformationTechnology/MobileWebAppDevelopmentCertificate.pdf">Mobile web app development</a>


## Jobs
- Freelancing contracts:
  - <a href="https://www.docracy.com/0kpa5hfcobb/freelance-developer-contract">https://www.docracy.com/0kpa5hfcobb/freelance-developer-contract</a>
  - <a href="https://gist.github.com/malarkey/4031110">https://gist.github.com/malarkey/4031110</a>
  - <a href="https://github.com/ashedryden/freelance-contract">https://github.com/ashedryden/freelance-contract</a>
  - <a href="https://gist.github.com/reubano/344656121394ef7ff2048ca8b006f7d2">https://gist.github.com/reubano/344656121394ef7ff2048ca8b006f7d2</a>
- Freelancing tips/guides/tutorials:
  - <a href="https://gist.github.com/mdang/ef3669d4f266c62c3312">https://gist.github.com/mdang/ef3669d4f266c62c3312</a>
  - <a href="http://www.incomeinsiders.com/tag/freelance-programmer-contract/">http://www.incomeinsiders.com/tag/freelance-programmer-contract/</a>
- Remote/freelancing:
  - <a href="https://github.com/engineerapart/TheRemoteFreelancer">https://github.com/engineerapart/TheRemoteFreelancer</a>
  - Indeed/indeed prime
  - Upwork/Fiverr
  - <a href="https://weworkremotely.com/categories/remote-programming-jobs">Weworkremotely programming jobs</a>
- <a href="http://jessicahische.is/helpingyouanswer">Repsonding to freelancing gig offers</a>
- <a href="https://www.codementor.io">Codementor</a>
- <a href="https://junilearning.com/">Juni</a>
- <a href="http://generalassemb.ly/how-we-work/teach-at-general-assembly">General Assembly teaching</a>
- <a href="https://jobs.chegg.com/search-results?category=Education">Thinkful web dev instructor</a>
- <a href="https://www.codeforamerica.org/jobs">Code for America</a>
- <a href="https://slack.com/careers/1852134/software-engineering-internship">Slack internship</a>
- <a href="https://jobs.ccsf.edu/">CCSF professor</a>


## Interview prep
- <a href="https://docs.google.com/document/d/1L2nqcMLxQeFHVd9ZOfgzZTjxWZsJLJe65rAzKfmldsM/edit">Interview questions</a>
- <a href="http://meetupresources.herokuapp.com/index.html">Interview algorithms and tips</a>
- <a href="http://kelukelu.me/interview/questions.html">Assorted interview tips</a>
- <a href="https://github.com/WomenWhoCode/Algorithms-InterviewPrep/wiki">Women Who Code Interview Prep</a>
- Gayle McDowell:
  - <a href="https://www.youtube.com/watch?v=rEJzOhC5ZtQ">talk at Canadian University Software Engineering Conference</a>
  - <a href="https://www.youtube.com/watch?v=1fqxMuPmGak">Ask Me Anything video (see the top comment with all the links to the individual questions)</a>


## Stack Overflow
- Users I like:
  - <a href="https://stackoverflow.com/users/224132/">https://stackoverflow.com/users/224132/</a>
  - <a href="https://stackoverflow.com/users/895245/">https://stackoverflow.com/users/895245/</a>
  - <a href="https://stackoverflow.com/users/5459839/">https://stackoverflow.com/users/5459839/</a>
  - <a href="https://stackoverflow.com/users/3000206/">https://stackoverflow.com/users/3000206/</a>
  - <a href="https://stackoverflow.com/users/168657/">https://stackoverflow.com/users/168657/</a>
  - <a href="https://stackoverflow.com/users/559737/">https://stackoverflow.com/users/559737/</a>
  - <a href="https://stackoverflow.com/users/385378/">https://stackoverflow.com/users/385378/</a>
  - <a href="https://stackoverflow.com/users/1204143/">https://stackoverflow.com/users/1204143/</a>
  - <a href="https://stackoverflow.com/users/128511/">https://stackoverflow.com/users/128511/</a>
  - <a href="https://stackoverflow.com/users/501557/">https://stackoverflow.com/users/501557/</a>
  - <a href="https://stackoverflow.com/users/1566221/">https://stackoverflow.com/users/1566221/</a>


## Fun
- <a href="https://stackoverflow.com/questions/172303/is-there-a-regular-expression-to-detect-a-valid-regular-expression">Regex to validate another regex</a>
- <a href="https://en.wikipedia.org/wiki/Quine_(computing)">Quine</a>
- <a href="https://github.com/leachim6/hello-world">Hello World in every language</a>
- <a href="http://www.99-bottles-of-beer.net/">99 bottles of beer in 1500 different languages</a>
- <a href="https://codegolf.stackexchange.com/questions/11880/build-a-working-game-of-tetris-in-conways-game-of-life">Tetris written in Conway's Game of Life</a>
- FizzBuzz stuff:
  - <a href="http://wiki.c2.com/?FizzBuzzTest">http://wiki.c2.com/?FizzBuzzTest</a>
  - <a href="https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition">https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition</a>
- <a href="https://git-man-page-generator.lokaltog.net/">Git man page generator</a>
