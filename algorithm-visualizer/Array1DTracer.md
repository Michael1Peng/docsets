[Skip to content](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array1DTracer#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array1DTracer) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array1DTracer) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array1DTracer) to refresh your session.Dismiss alert

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


# Array1DTracer

[Jump to bottom](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array1DTracer#wiki-pages-box)

Jason Park edited this page Jul 13, 2018
·
[1 revision](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array1DTracer/_history)

# Array1DTracer

[Permalink: Array1DTracer](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array1DTracer#array1dtracer)

Visualize a one-dimensional array into a table. [Usage](https://github.com/search?q=Array1DTracer+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code)

## Methods

[Permalink: Methods](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/Array1DTracer#methods)

| Name | Description |  |
| --- | --- | --- |
| **Array1DTracer** | Create an Array1DTracer object. | [Usage](https://github.com/search?q=Array1DTracer+Array1DTracer+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>new Array1DTracer(String title = "Array1DTracer")<br>``` |
| **set** | Set `array1d` to visualize. | [Usage](https://github.com/search?q=Array1DTracer+set+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer set(Object[] array1d = [])<br>``` |
| **reset** | Reset data. | [Usage](https://github.com/search?q=Array1DTracer+reset+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer reset()<br>``` |
| **delay** | Pause to show changes in all tracers. | [Usage](https://github.com/search?q=Array1DTracer+delay+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer delay()<br>``` |
| **patch** | Notify that the value at ( `x`) has been changed to `v`. | [Usage](https://github.com/search?q=Array1DTracer+patch+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer patch(int x, Object v)<br>``` |
| **depatch** | Stop notifying that the value at ( `x`) has been changed. | [Usage](https://github.com/search?q=Array1DTracer+depatch+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer depatch(int x)<br>``` |
| **select** | Select ( `x`). | [Usage](https://github.com/search?q=Array1DTracer+select+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer select(int x)<br>``` |
| **select** | Select from ( `sx`) to ( `ex`). | [Usage](https://github.com/search?q=Array1DTracer+select+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer select(int sx, int ex)<br>``` |
| **deselect** | Stop selecting ( `x`). | [Usage](https://github.com/search?q=Array1DTracer+deselect+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer deselect(int x)<br>``` |
| **deselect** | Stop selecting from ( `sx`) to ( `ex`). | [Usage](https://github.com/search?q=Array1DTracer+deselect+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer deselect(int sx, int ex)<br>``` |
| **chart** | Synchronize data with `chartTracer`. | [Usage](https://github.com/search?q=Array1DTracer+chart+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>Array1DTracer chart(ChartTracer chartTracer)<br>``` |

##### Clone this wiki locally

You can’t perform that action at this time.