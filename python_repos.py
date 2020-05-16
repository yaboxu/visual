"""获取github中星数最多的python项目"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用，存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中，这个API返回JSON格式的信息
response_dict = r.json() 

print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])
print("Incomplete results:", response_dict['incomplete_results'])

# 研究有关仓库的信息
repo_dicts = response_dict['items']

names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
   
    if repo_dict['description']:
        plot_dict = {
            'value':repo_dict['stargazers_count'],
            'label':repo_dict['description'],
            'xlink':repo_dict['html_url'],
            }
    else:
        plot_dict = {
            'value':repo_dict['stargazers_count'],
            'label':'none',
            'xlink':repo_dict['html_url'],
            }
    plot_dicts.append(plot_dict)
    
# 可视化pygal
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-starred python projects on github'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')

# 浏览器file:///C:/users/Administrator/Desktop/python_work/keshihua/python_repos.svg

