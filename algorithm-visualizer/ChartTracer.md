[Skip to content](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/ChartTracer#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/ChartTracer) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/ChartTracer) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/ChartTracer) to refresh your session.Dismiss alert

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


# ChartTracer

[Jump to bottom](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/ChartTracer#wiki-pages-box)

Jason Park edited this page Jul 13, 2018
·
[1 revision](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/ChartTracer/_history)

# ChartTracer

[Permalink: ChartTracer](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/ChartTracer#charttracer)

Visualize a one-dimensional array into a bar chart. [Usage](https://github.com/search?q=ChartTracer+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code)

## Methods

[Permalink: Methods](https://github.com/algorithm-visualizer/algorithm-visualizer/wiki/ChartTracer#methods)

| Name | Description |  |
| --- | --- | --- |
| **ChartTracer** | Create a ChartTracer object. | [Usage](https://github.com/search?q=ChartTracer+ChartTracer+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>new ChartTracer(String title = "ChartTracer")<br>``` |
| **set** | Set `array1d` to visualize. | [Usage](https://github.com/search?q=ChartTracer+set+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer set(Object[] array1d = [])<br>``` |
| **reset** | Reset data. | [Usage](https://github.com/search?q=ChartTracer+reset+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer reset()<br>``` |
| **delay** | Pause to show changes in all tracers. | [Usage](https://github.com/search?q=ChartTracer+delay+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer delay()<br>``` |
| **patch** | Notify that the value at ( `x`) has been changed to `v`. | [Usage](https://github.com/search?q=ChartTracer+patch+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer patch(int x, Object v)<br>``` |
| **depatch** | Stop notifying that the value at ( `x`) has been changed. | [Usage](https://github.com/search?q=ChartTracer+depatch+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer depatch(int x)<br>``` |
| **select** | Select ( `x`). | [Usage](https://github.com/search?q=ChartTracer+select+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer select(int x)<br>``` |
| **select** | Select from ( `sx`) to ( `ex`). | [Usage](https://github.com/search?q=ChartTracer+select+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer select(int sx, int ex)<br>``` |
| **deselect** | Stop selecting ( `x`). | [Usage](https://github.com/search?q=ChartTracer+deselect+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer deselect(int x)<br>``` |
| **deselect** | Stop selecting from ( `sx`) to ( `ex`). | [Usage](https://github.com/search?q=ChartTracer+deselect+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer deselect(int sx, int ex)<br>``` |
| **chart** | Synchronize data with `chartTracer`. | [Usage](https://github.com/search?q=ChartTracer+chart+repo%3Aalgorithm-visualizer%2Falgorithms&type=Code) |
| ```<br>ChartTracer chart(ChartTracer chartTracer)<br>``` |

##### Clone this wiki locally

You can’t perform that action at this time.