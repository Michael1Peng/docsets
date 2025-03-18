[Skip to content](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array2DTracer#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array2DTracer) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array2DTracer) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array2DTracer) to refresh your session.Dismiss alert

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


# Array2DTracer

[Jump to bottom](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array2DTracer#wiki-pages-box)

Jason Park edited this page Jul 13, 2018
·
[1 revision](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array2DTracer/_history)

# Array2DTracer

[Permalink: Array2DTracer](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array2DTracer#array2dtracer)

Visualize a two-dimensional array into a table. [Usage](https://github.com/search?q=Array2DTracer+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code)

## Methods

[Permalink: Methods](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array2DTracer#methods)

| Name | Description |  |
| --- | --- | --- |
| **Array2DTracer** | Create an Array2DTracer object. | [Usage](https://github.com/search?q=Array2DTracer+Array2DTracer+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>new Array2DTracer(String title = "Array2DTracer")<br>``` |
| **set** | Set `array2d` to visualize. | [Usage](https://github.com/search?q=Array2DTracer+set+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer set(Object[][] array2d = [])<br>``` |
| **reset** | Reset data. | [Usage](https://github.com/search?q=Array2DTracer+reset+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer reset()<br>``` |
| **delay** | Pause to show changes in all tracers. | [Usage](https://github.com/search?q=Array2DTracer+delay+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer delay()<br>``` |
| **patch** | Notify that the value at ( `x`, `y`) has been changed to `v`. | [Usage](https://github.com/search?q=Array2DTracer+patch+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer patch(int x, int y, Object v)<br>``` |
| **depatch** | Stop notifying that the value at ( `x`, `y`) has been changed. | [Usage](https://github.com/search?q=Array2DTracer+depatch+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer depatch(int x, int y)<br>``` |
| **select** | Select ( `x`, `y`). | [Usage](https://github.com/search?q=Array2DTracer+select+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer select(int x, int y)<br>``` |
| **select** | Select from ( `sx`, `sy`) to ( `ex`, `ey`). | [Usage](https://github.com/search?q=Array2DTracer+select+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer select(int sx, int sy, int ex, int ey)<br>``` |
| **selectRow** | Select from ( `x`, `sy`) to ( `x`, `ey`). | [Usage](https://github.com/search?q=Array2DTracer+selectRow+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer selectRow(int x, int sy, int ey)<br>``` |
| **selectCol** | Select from ( `sx`, `y`) to ( `ex`, `y`). | [Usage](https://github.com/search?q=Array2DTracer+selectCol+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer selectCol(int y, int sx, int ex)<br>``` |
| **deselect** | Stop selecting ( `x`, `y`). | [Usage](https://github.com/search?q=Array2DTracer+deselect+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer deselect(int x, int y)<br>``` |
| **deselect** | Stop selecting from ( `sx`, `sy`) to ( `ex`, `ey`). | [Usage](https://github.com/search?q=Array2DTracer+deselect+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer deselect(int sx, int sy, int ex, int ey)<br>``` |
| **deselectRow** | Stop selecting from ( `x`, `sy`) to ( `x`, `ey`). | [Usage](https://github.com/search?q=Array2DTracer+deselectRow+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer deselectRow(int x, int sy, int ey)<br>``` |
| **deselectCol** | Stop selecting from ( `sx`, `y`) to ( `ex`, `y`). | [Usage](https://github.com/search?q=Array2DTracer+deselectCol+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array2DTracer deselectCol(int y, int sx, int ex)<br>``` |

##### Clone this wiki locally

You can’t perform that action at this time.