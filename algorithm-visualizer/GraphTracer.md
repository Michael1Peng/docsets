[Skip to content](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/GraphTracer#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/GraphTracer) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/GraphTracer) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/GraphTracer) to refresh your session.Dismiss alert

[algorithm-visualizer](https://github.com/algorithm-visualizer)/ **[algorithm-visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer)** Public

- Sponsor







# Sponsor algorithm-visualizer/algorithm-visualizer



















##### External links









[https://www.paypal.com/cgi-bin/webscr?cmd=\_donations&business=CFS8Y6G3E29UA](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=CFS8Y6G3E29UA)









[Learn more about funding links in repositories](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository).




[Report abuse](https://github.com/contact/report-abuse?report=algorithm-visualizer%2Falgorithm-visualizer+%28Repository+Funding+Links%29)

- [Notifications](https://github.com/login?return_to=%2Falgorithm-visualizer%2Falgorithm-visualizer) You must be signed in to change notification settings
- [Fork\\
7.3k](https://github.com/login?return_to=%2Falgorithm-visualizer%2Falgorithm-visualizer)
- [Star\\
47.2k](https://github.com/login?return_to=%2Falgorithm-visualizer%2Falgorithm-visualizer)


# GraphTracer

[Jump to bottom](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/GraphTracer#wiki-pages-box)

Jason Park edited this page Dec 3, 2018
·
[2 revisions](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/GraphTracer/_history)

# GraphTracer

[Permalink: GraphTracer](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/GraphTracer#graphtracer)

Visualize an adjacency matrix into a graph. [Usage](https://github.com/search?q=GraphTracer+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code)

## Methods

[Permalink: Methods](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/GraphTracer#methods)

| Name | Description |  |
| --- | --- | --- |
| **GraphTracer** | Create a GraphTracer object. | [Usage](https://github.com/search?q=GraphTracer+GraphTracer+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>new GraphTracer(String title = "GraphTracer")<br>``` |
| **set** | Set `array2d` to visualize. | [Usage](https://github.com/search?q=GraphTracer+set+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer set(Object[][] array2d = [])<br>``` |
| **reset** | Reset data. | [Usage](https://github.com/search?q=GraphTracer+reset+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer reset()<br>``` |
| **delay** | Pause to show changes in all tracers. | [Usage](https://github.com/search?q=GraphTracer+delay+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer delay()<br>``` |
| **directed** | Make the graph directed. | [Usage](https://github.com/search?q=GraphTracer+directed+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer directed(boolean isDirected = true)<br>``` |
| **weighted** | Make the graph weighted. | [Usage](https://github.com/search?q=GraphTracer+weighted+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer weighted(boolean isWeighted = true)<br>``` |
| **addNode** | Add a node. | [Usage](https://github.com/search?q=GraphTracer+addNode+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer addNode(Object id, double weight = null, double x = 0, double y = 0, int visitedCount = 0, int selectedCount = 0)<br>``` |
| **updateNode** | Update a node. | [Usage](https://github.com/search?q=GraphTracer+updateNode+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer updateNode(Object id, double weight = undefined, double x = undefined, double y = undefined, int visitedCount = undefined, int selectedCount = undefined)<br>``` |
| **removeNode** | Remove a node. | [Usage](https://github.com/search?q=GraphTracer+removeNode+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer removeNode(Object id)<br>``` |
| **addEdge** | Add an edge connecting from `source` to `target`. | [Usage](https://github.com/search?q=GraphTracer+addEdge+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer addEdge(Object source, Object target, double weight = null, int visitedCount = 0, int selectedCount = 0)<br>``` |
| **updateEdge** | Update an edge connecting from `source` to `target`. | [Usage](https://github.com/search?q=GraphTracer+updateEdge+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer updateEdge(Object source, Object target, double weight = undefined, int visitedCount = undefined, int selectedCount = undefined)<br>``` |
| **removeEdge** | Remove an edge connecting from `source` to `target`. | [Usage](https://github.com/search?q=GraphTracer+removeEdge+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer removeEdge(Object source, Object target)<br>``` |
| **layoutCircle** | Arrange nodes on a circular layout. | [Usage](https://github.com/search?q=GraphTracer+layoutCircle+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer layoutCircle()<br>``` |
| **layoutTree** | Arrange nodes on a tree layout having `root` as its root node. | [Usage](https://github.com/search?q=GraphTracer+layoutTree+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer layoutTree(Object root = 0, boolean sorted = false)<br>``` |
| **layoutRandom** | Arrange nodes randomly. | [Usage](https://github.com/search?q=GraphTracer+layoutRandom+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer layoutRandom()<br>``` |
| **visit** | Visit `target` from `source`. | [Usage](https://github.com/search?q=GraphTracer+visit+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer visit(Object target, Object source = null, double weight = null)<br>``` |
| **leave** | Return from `target` to `source`. | [Usage](https://github.com/search?q=GraphTracer+leave+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer leave(Object target, Object source = null, double weight = null)<br>``` |
| **select** | Select `target` from `source`. | [Usage](https://github.com/search?q=GraphTracer+select+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer select(Object target, Object source = null)<br>``` |
| **deselect** | Stop selecting `target` from `source`. | [Usage](https://github.com/search?q=GraphTracer+deselect+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer deselect(Object target, Object source = null)<br>``` |
| **log** | Log graph traversals. | [Usage](https://github.com/search?q=GraphTracer+log+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>GraphTracer log(LogTracer logTracer)<br>``` |

##### Clone this wiki locally

You can’t perform that action at this time.