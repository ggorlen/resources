## General ##
+ Bit twiddling hacks: http://graphics.stanford.edu/~seander/bithacks.html
+ Do projects from Data Structures text
+ organize mp3s: beets.io & https://www.discogs.com/developers/
+ Car talk puzzlers: https://developmentality.wordpress.com/tag/car-talk/


## Project Euler ##
+ Project Euler todo: 81, 99, 77, 78, 112, 345
+ #93 can also be solved using Integer Linear Programming (https://pythonhosted.org/PuLP/CaseStudies/a_sudoku_problem.html)
+ #84 Monopoly is one of the best.  Worth solving using both simulation (I used first-class functions) and stochastic matrix (I used numpy).  Working out the initial probabilities for the stochastic matrix requires only basic probability, but it's tricky.


## Fractals and L-systems ##
+ Book on JS fractals: http://www.playingwithchaos.net/
+ L-systems user notes/manual: http://paulbourke.net/fractals/lsys/
+ L-system examples: https://10klsystems.wordpress.com/examples/
+ 2d L-systems: http://mathforum.org/advanced/robertd/lsys2d.html
+ Full-featured L-systems app: http://www.kevs3d.co.uk/dev/lsystems/
+ Hausdorff fractals list: https://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension
+ Abelian sandpiles: https://en.wikipedia.org/wiki/Abelian_sandpile_model 
+ Koch snowflake: https://en.wikipedia.org/wiki/Koch_snowflake
+ Sierpinski carpet: https://en.wikipedia.org/wiki/Sierpinski_carpet
+ Rose: https://en.wikipedia.org/wiki/Rose_(mathematics)
+ https://en.wikipedia.org/wiki/Chaos_game
+ https://en.wikipedia.org/wiki/Barnsley_fern


## Tiling and packing ##
+ Rhombile tiling: https://en.wikipedia.org/wiki/Rhombille_tiling
+ Tangrams: https://en.wikipedia.org/wiki/Tangram
+ https://en.wikipedia.org/wiki/Tiling_puzzle
+ https://thebrickinthesky.wordpress.com/2013/03/17/l-systems-and-penrose-p3-in-inkscape
+ Girih tiles: https://en.wikipedia.org/wiki/Girih_tiles
+ https://en.wikipedia.org/wiki/Wallpaper_group
+ https://morphingtiling.wordpress.com/page/2/
+ https://transcendentcode.wordpress.com/
+ Penrose tiling: http://preshing.com/20110831/penrose-tiling-explained/ 
+ Penrose tiling: http://www.math.ubc.ca/~cass/courses/m308-02b/projects/schweber/penrose.html
+ https://en.wikipedia.org/wiki/Substitution_tiling
+ isometic JS example: http://jsfiddle.net/a4ZbG/
+ https://en.wikipedia.org/wiki/Packing_problems
+ https://en.wikipedia.org/wiki/Truncated_hexagonal_tiling#Triakis_triangular_tiling


## Physics simulations ##
+ Coding math tutorial: https://www.youtube.com/watch?v=11ZmRlR7sOQ 
+ Khan Academy natural simulations: https://www.khanacademy.org/computing/computer-programming/programming-natural-simulations/programming-vectors/p/project-computational-creatures
+ Double pendulum: 
  + https://en.wikipedia.org/wiki/Double_pendulum 
  + https://www.youtube.com/watch?v=neh86u7_TIk
+ Game physics cookbook: http://proquest.safaribooksonline.com/9781787123663
+ Nature in Code book: https://leanpub.com/natureincode
+ Brief intro to sin & cos: https://inventwithpython.com/blog/2012/07/18/using-trigonometry-to-animate-bounces-draw-clocks-and-point-cannons-at-a-target/


## Scratch and Snap ##
+ http://www.ocsmag.com/2016/07/12/dump-scratch-use-blockly-or-snap-instead/
+ https://wiki.scratch.mit.edu/wiki/List_of_Mathematical_Functions_Done_in_Scratch
+ https://wiki.scratch.mit.edu/wiki/Recursion_and_Fractals#Creating_the_Koch_Curve
+ https://inventwithscratch.com/
+ https://www.youtube.com/playlist?list=PL0-84-yl1fUkall6a14nqzXpG79-RgI1F
+ https://www.youtube.com/playlist?list=PL0-84-yl1fUlLJvyC1s5L8rs5ECn3lPx4
+ https://wiki.scratch.mit.edu/wiki/Array#Multidimensional_Arrays_in_Scratch


## Interview algorithms ##
+ DP: https://en.wikipedia.org/wiki/Dynamic_programming
+ DP coin change: http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/
+ MIT open courseware DP lecture: https://www.youtube.com/watch?v=ocZMDMZwhCY
+ Algs/DP: https://people.eecs.berkeley.edu/~vazirani/algorithms/chap6.pdf
+ Fermat's factorization method: https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
+ Floyd Warshall algorithm: http://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm
+ Dijkstra's algorithm: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
+ Memoization: http://www.python-course.eu/python3_memoization.php
+ Euclid's algorithm  http://andreinc.net/2010/12/11/euclids-algorithm-reducing-fraction-to-lowest-terms/
+ Simplify a fraction: http://codereview.stackexchange.com/questions/66450/simplify-a-fraction
+ Basil & Fabian: http://blog.jamisbuck.org/
+ Knapsack problem
+ The three witches in Hamlet can brew any potion provided they have the right ingredients. Suppose that five ingredients are necessary in making a health potion: eye of newt (eon), toe of frog (tof), wool of bat (wob), adder’s fork (af), and tooth of wolf (tow). Four reactions can occur between these ingredients: 
  - 4 eon + 2 wob = 3 af + 4 tow 
  - 3 tow + 1 tof = 2 eon 
  - 1 wob + 2 af = 1 tof 
  - 4 tof + 7 tow + 2 af = 1 health potion 
  Assuming you can control the order of reactions, write a program that can calculate the maximum number of health potions one can brew   with a given amount of ingredients. Here is example output: If I have 34 eon, 59 tof, 20 wob, 5 af, and 20 tow, I can make seven   health potions. 
+ The "correct change" problem looks like it's equivalent to the "subset sum" problem  (https://en.wikipedia.org/wiki/Subset_sum_problem), which is a special case of the knapsack problem.  Wikipedia says these are all NP, but efficiency can be improved by dynamic programming. That's why I'm thinking a transposition table may help.
+ Permute a string: http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
+ Find combinations of a string in another string: http://stackoverflow.com/questions/24720332/c-find-all-possible-combinations-of-a-string-in-another-string 
+ Sum numbers in a list: http://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number
+ Good DP problem: http://www.opengarden.com/jobs.html
+ Tree traversal construction: http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
+ Determine if a tree is a BST: https://www.youtube.com/watch?v=H13iz0rbeeo


## Mazes ##
  + Think Labyrinth: http://www.astrolog.org/labyrnth/algrithm.htm
  + Buckblog maze generation algorithm overview: http://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap


## Cellular automata ##
+ https://en.wikipedia.org/wiki/Turmite
+ conway's game of life https://en.wikipedia.org/wiki/Cellular_automaton


## Puzzles ##
+ Amazing site--Erich Friendman's puzzle palace: http://www2.stetson.edu/~efriedma/
+ Mindsports (links resource): http://www.mindsports.nl/index.php/puzzle-links
+ Zendoku puzzle generation: http://garethrees.org/2007/06/10/zendoku-generation/#section-4
+ Sudoku solving algorithms: https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
+ Mondrian puzzle: https://www.youtube.com/watch?v=49KvZrioFB0
+ http://nikoli.co.jp/en/puzzles/
+ https://en.wikipedia.org/wiki/Nonogram
+ https://en.wikipedia.org/wiki/Slothouber%E2%80%93Graatsma_puzzle 
+ https://en.wikipedia.org/wiki/Mathematical_puzzle
+ Soma cube
+ Assorted logic games: https://www.youtube.com/channel/UCEPZPgtnTvj2F3qTCLfaP4w
+ https://en.wikipedia.org/wiki/Lights_Out_(game)


## Visual/animations ##
+ Inspiring: http://zreference.com/projects/graphics/
+ Also inspiring: https://bit101.github.io/lab/dailies/170413.html
+ Fibonacci spiral
+ Architecture: look for triangle perspective designs, escher...https://s-media-cache-ak0.pinimg.com/564x/d6/ff/64/d6ff6450173c6410c919b06e07958227.jpg
+ Simple Python graphics library: https://www.rose-hulman.edu/Users/faculty/young/CS-Classes/resources/Python/ZelleGraphics.html
+ Do a visual plotting the orthocenter, medicenter, and circumcenter of a triangle
+ Animated sorts and searches etc
+ Do a recursive ripple GUI program
+ Canvas stack http://arc.id.au/CanvasLayers.html
+ ThreeJS: https://threejs.org/
+ JSXGraph: https://jsxgraph.uni-bayreuth.de/wiki/index.php/Category:Examples
+ Do a WebGLRenderer tutorial!
+ Cool examples/inspiration: http://entibo.fr/


## Game AI ##
+ https://www.codeproject.com/Articles/37024/Simple-AI-for-the-Game-of-Breakthrough
+ Write a correspondence chess app for your homepage in PHP
+ https://en.wikipedia.org/wiki/SSS*
+ https://en.wikipedia.org/wiki/Principal_variation_search
+ https://en.wikipedia.org/wiki/MTD-f
+ https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search
+ https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
+ https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/
+ http://cwoebker.com/posts/tic-tac-toe
+ http://neverstopbuilding.com/minimax
+ https://www.leaseweb.com/labs/2013/12/python-tictactoe-tk-minimax-ai/
+ mcts: http://mcts.ai/code/java.html
+ https://en.wikipedia.org/wiki/Negamax


## Games to program ##
+ Microsoft Entertainment Pack: https://en.wikipedia.org/wiki/Microsoft_Entertainment_Pack
+ Code hexapawn JS ♟
+ Dots and boxes https://www.youtube.com/watch?v=KboGyIilP6k
+ Breakthru: https://en.wikipedia.org/wiki/Breakthru_(board_game)
+ Beast: https://en.wikipedia.org/wiki/Beast_(video_game)
+ PHP game scripts: https://www.ibm.com/developerworks/library/os-php-gamescripts1/
+ Pygame: http://inventwithpython.com/pygame/
+ Program arcade games: http://programarcadegames.com/
+ BASIC games: http://www.atariarchives.org/basicgames/
+ Nim: https://en.wikipedia.org/wiki/Nim
+ Emily's pegs game http://www.instructables.com/id/Peg-Game-IQ-Test-Solution/
+ Fire & Ice
+ Connect 4
+ Freerice clone
+ The Mill board game
+ Solitaire/patience
+ Lemmings
+ Hive
+ Lines of action: https://dke.maastrichtuniversity.nl/m.winands/loa/
+ 2048
+ Ultimate tic tac toe
+ https://en.wikipedia.org/wiki/Marble_Madness
+ https://en.wikipedia.org/wiki/Loco-Motion_(video_game)
+ Hnefatafl
+ Go
+ Boggle
+ Mastermind https://en.wikipedia.org/wiki/Mastermind_(board_game)
+ https://en.wikipedia.org/wiki/List_of_abstract_strategy_games
+ Reversi: http://inventwithpython.com/chapter15.html
+ dodge falling objects game--rotation component like super hexagon?
+ sidescroller where you build steps to get your dude over obstacles instead of jump button
+ flappy bird / side scroll platformer with jump button only
+ try frequency distribution array for card games/poker problem
+ snake: 2 player versions, add obstacles, display score text after losing?
+ ASCII games: 
  + http://ifarchive.org/
  + http://www.8bs.com/othrdnld/manuals/publications.shtml
  + https://en.wikipedia.org/wiki/Jotto
  + https://en.wikipedia.org/wiki/NetHack
  + http://www.iancgbell.clara.net/elite/text/index.htm
+ God wars mud
+ Boulder dash
+ Digger


## Cryptography ##
+ http://security.stackexchange.com/questions/45963/diffie-hellman-key-exchange-in-plain-english


## Machine learning/big data ##
+ https://douweosinga.com/projects/
+ https://github.com/wasd12345


## JS/CSS/front end ##
+ Callbacks: http://javascriptissexy.com/understand-javascript-callback-functions-and-use-them/
+ CSS modals (drop down boxes): http://www.w3schools.com/howto/howto_css_modals.asp iframe
+ JS todo list: http://docs.railsbridge.org/javascript-to-do-list/adding_an_item
+ Jekyll blog: https://www.youtube.com/watch?v=xdxfyFS3pog & https://jekyllrb.com/docs/installation/
+ Bitballoon for hosting web apps: https://www.bitballoon.com


## PHP ##
+ AJAX
  + http://stackoverflow.com/questions/23980733/jquery-ajax-file-upload-php 
  + http://stackoverflow.com/questions/2269307/using-jquery-ajax-to-call-a-php-function
  + https://stackoverflow.com/questions/5004233/jquery-ajax-post-example-with-php
  + ajax/php tutorial: http://www.tizag.com/ajaxTutorial/ajaxxmlhttprequest.php
  + ajax/php mailing list for label: https://www.sitepoint.com/use-ajax-php-build-mailing-list/
+ PHP WP plugins
+ Make a simple tape label CMS; host on heroku?
  
  
## Python ##
+ Automate the boring stuff: https://automatetheboringstuff.com/#toc
+ Python data structures & algorithms
  + http://interactivepython.org/runestone/static/pythonds/index.html
  + http://www.brpreiss.com/books/opus7/
+ Computer vision with python: http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf
+ Natural language processing with Python:
  + http://www.nltk.org/book/
+ Flask:
  + https://exploreflask.com/en/latest/
  + https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
  + http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/
+ Python yield keyword/iterators: http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
+ Effective Python: http://www.effectivepython.com/
+ Play with Python turtle chase from Think Python
+ Python exercises: http://www.ling.gu.se/~lager/python_exercises.html
+ Python from Java: http://dirtsimple.org/2004/12/python-is-not-java.html
+ http://interactivepython.org/courselib/static/thinkcspy/index.html
+ https://www.learneroo.com/subjects/3
+ https://anshbansal.wordpress.com/programming-links/
+ http://www.megantaylor.org/2013/04/17/i-finished-codecademy-now-what/
+ http://pygame.org/news.html
+ https://www.coursera.org/course/interactivepython
+ http://pythonchallenge.com/
+ http://www.interactivepython.org/runestone/default/user/login?_next=/runestone/default/index


## Java ##
+ Good Java web framework for learning generics: https://struts.apache.org/ 
+ Google style guide: https://google.github.io/styleguide/javaguide.html
+ Edx intro to Java: https://www.edx.org/course/introduction-java-programming-part-2-hkustx-comp102-2x-0
+ Java sorting algorithms: http://java2novice.com/java-sorting-algorithms/
+ Java send HTTP request: http://stackoverflow.com/questions/2793150/using-java-net-urlconnection-to-fire-and-handle-http-requests
+ Java send email: http://stackoverflow.com/questions/3649014/send-email-using-java


## Ruby ##
+ http://poignant.guide/book/chapter-6.html
+ Rails mailing list http://aspiringwebdev.com/e-mail-in-rails-with-mailchimp-and-mandrill-a-comprehensive-guide


## C++ ##
+ C++ sfml for games


## Bots ##
+ Twitter bot hosting:
  + https://botwiki.org/tutorials/twitterbots/
+ Tweet image:
  + http://stackoverflow.com/questions/24692147/how-to-upload-image-and-status-to-twitter-using-twitter4j
  + https://botwiki.org/tutorials/make-an-image-posting-twitter-bot/  
+ Java robot project: play online pianos at http://virtualpiano.net/
+ Ideas for bots:
  + Bot where you can teach it words by tweeting @ it
  + Web crawler: http://scrapy.org/
  + Chess vote bot with an ongoing game?
  + Game bots: http://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117
  + Something quote-based like David Markson
+ FB bots:
  + http://nodotcom.org/python-facebook-tutorial.html
  + http://stackoverflow.com/questions/25400841/jsoup-how-to-get-content-of-facebook-event-page-as-logged-in-user
  + http://jodd.org/doc/jerry/facebook-bot.html
+ Java web robot: https://dadicy.wordpress.com/2007/10/17/how-to-write-a-simple-web-robot-in-java/
+ Tumblr bots:
  + https://epicjefferson.wordpress.com/2014/09/28/python-to-tumblr/
  + http://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
  + http://verythorough.tumblr.com/post/101348170234/creating-a-twitterbot-in-python


## Minecraft ##
+ Minecraft modding tutorial https://www.youtube.com/watch?v=2_qM-Z0IQ4k
+ Minecraft programming http://minecraft.gamepedia.com/Mods/Creating_mods
