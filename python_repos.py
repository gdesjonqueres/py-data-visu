import requests
import pygal

from pygal.style import LightGreenStyle as LGS

r = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars')
if not r.status_code == 200:
    exit('Error fetching data')

repo_list = r.json()

names, stars = [], []
for repo in repo_list['items'][:20]:
    # print('{:6d} - {:30s} ==> {}'.format(repo['stargazers_count'], repo['name'], repo['description']))
    names.append(repo['name'])
    # stars.append(repo['stargazers_count'])
    rep = {
        'value': repo['stargazers_count'],
        'xlink': repo["html_url"]}
    if repo['description']:
        rep['label'] = repo['description']
    else:
        rep['label'] = 'No description'
    stars.append(rep)

my_style = LGS(font_family='googlefont:Raleway',
                  value_font_size=20,
                  tooltip_font_size=10)
hist = pygal.Bar(value_formatter=lambda x: '{:,}'.format(x), style=my_style)

hist.title = str(len(names)) + " Most popular Python projects on GithHub"
hist.x_labels = names
hist.x_label_rotation = 20
hist.y_title = "Number of stars"

hist.add('Projects', stars)
hist.render_to_file('github_repos.svg')
