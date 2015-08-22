# udpy
Side project to get some practice with out of memory algorithms

# Use case

Out of memory exploratory data management. You have multi-terabyte sized data files on a hard drive that haven't been loaded into a database and you need to explore the data to figure out what needs to be loaded. Coreutils are too low level for exploratory analysis, but other exploratory tools require the data to be loaded into RAM.

# Alternatives that don't quite solve the problem
* Coreutils - Great tools for out of memory data management, but very low level. Creating a grouped summary table of means is not a one-line task as it should be.
* R/Python/Scala - Most tools break when data size is greater than RAM capacity. You can always code in a style that stores everything on disk, but that approach tends to be verbose and slow. A faster approach is to properly deal with spillage from RAM to disk, but that's verbose and requires careful thought. Also not a one-line solution.
* Databases - These almost satisfy the use case. SQL queries are flexible and compact. They can also be fully optimized for speed through a query optimizer. The memory optimizer will take care of disk reads and writes. The only drawbacks are that SQL queries are still a bit verbose for some tasks, loading data into a database comes with a great deal of overhead including schema definitions and waiting time. Finally, databases require tuning to work at full speed and require specific explicit knowledge about your hardware. Still not a one-line solution, but close, defiitely the best choice when outside of an exploratory context.
* [q utility](https://github.com/harelba/q) - This is great, possibly a bit verbose, and hard to extend, but if it deals with out of memory issues than it can be thoroughly optimized.

# How can we solve the issues with alternatives?
## Verbosity 
We can use Dplyr style syntax with unix pipes. Dplyr implements the functions select, filter, arrange, mutate, summarize, and groupby. This is extremely SQL-like, but has fewer query restrictions, for instance we can user filter without select in Dplyr, but we cannot use WHERE without SELECT in SQL. This is great for command line, but ultimately we lose the ability to choose query paths and some optimizations. 

Dplyr is usually paired with the 'magrittr', a IO Monad-like operator for R. Unix pipes are also IO Monad-like. Even though we are implementing a set of functions, there will be no need for ugly nested parathesis.

## Out of memory performance 
We can do a good job, but not perfect. Having a high level tool that works out of memory in itself is unique. Sadly, doing away with SQL means that we lose most query optimizations and have to take a unique dynamic approach. 

Dplyr syntax is at least in part compatible with the unix philosophy of small composable tools, this is relevant because we can take advantage of the unix pipe which runs concurrently. We can filter while we select, and it comes for free, but it would be more efficient to select while we filter. The order of execution is not entirely guaranteed in unix, so this is yet another dynamic component.

udpy -sel "variable1" | udpy -fil "variable2==2"

udpy -fil "variable2==2" | udpy -fil "variable1"

To take the burden off the user, we can use introspective dynamic optimization. That is, every function monitors its speed and attempts to set memory use parameters that optimize speed. This is concurrent chaos where little is guaranteed, but SHOULD do a decent job.

# Basic commands
udpy -sel "v1,v2"

udpy -fil "\<condition\>"

udpy -arr "v1,v2"

udpy -mut "\<expression\>"

udpy -sum "\<expression\>"

udpy -gby "v1,v2"
