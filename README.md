# Mkdocs-Github Theme for MkDocs

## About

Simple Theme for Mkdocs.

## Install

**<em>Required</em>**: Python 3.4+

If you haven't installed MkDocs yet, use the following command to install it:

<pre><code class="shell">$ pip install mkdocs</code></pre>
Next, navigate to a clean directory and create a new MkDocs project with the following command:

<pre><code class="shell">$ mkdocs new [projectname]</code></pre>
Replace `[projectname]` with the name of your project (without the brackets).

Then navigate to the root of your project directory:

<pre><code class="shell">$ cd [projectname]</code></pre>
## Install  Github Theme

with PIP `pip install mkdocs-github` or download with zip.

## Configuration

**mkdocs.yml** for install via **zip**

```yml
site_name: yourdocs
site_author: you
site_description: "you word."
site_keyword: "you word"

theme:
  name: null
  custom_dir: github
  highlightjs: true
  hljs_style: github
 
badge:
 github_repo: mkdocs-Github 
 github_user: g3xx
```

**mkdocs.yml** with install via **PIP**

```yml
site_name: yourdocs
site_author: you
site_description: "you word"
site_keyword: "your tag"

theme:
  name: github
  highlightjs: true
  hljs_style: github
 
badge:
 github_repo: antiFramework 
 github_user: g3xx

```

## License

**MIT** and CSS by [sindresorhus](https://github.com/sindresorhus/github-markdown-css)

