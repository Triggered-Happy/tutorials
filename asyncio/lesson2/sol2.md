Q.As you must have noticed, it is possible to start 2 tasks using this code, but they do not run efficiently (in terms of  I\O bound). Why? Explain how you found it?

A.Basically, the time.sleep command is I\O bound and therefore blocks us from running other things. This prevents us from improving utilization and improving efficiency.