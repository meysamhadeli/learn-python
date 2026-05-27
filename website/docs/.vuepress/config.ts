import { viteBundler } from '@vuepress/bundler-vite'
import { defineUserConfig } from 'vuepress'
import { plumeTheme } from 'vuepress-theme-plume'
import { contributionSidebar, courseSidebar } from './sidebar'

const repoName = 'learn-python'
const repoOwner = 'meysamhadeli'
const siteUrl = process.env.SITE_URL || process.env.URL || process.env.DEPLOY_PRIME_URL

export default defineUserConfig({
  lang: 'en-US',
  title: 'Learn Python',
  description: 'A practical Learn Python course published with VuePress Theme Plume.',
  base: '/',
  head: [
    ['meta', { name: 'theme-color', content: '#3776ab' }],
  ],
  bundler: viteBundler(),
  theme: plumeTheme({
    hostname: siteUrl,
    docsRepo: `${repoOwner}/${repoName}`,
    docsBranch: 'main',
    docsDir: 'website/docs',
    editLink: true,
    lastUpdated: {},
    contributors: false,
    changelog: false,
    search: {
      provider: 'local',
    },
    navbar: [
      {
        text: 'Course',
        link: '/',
      },
      {
        text: 'Contribution',
        link: '/contribution/',
      },
      {
        text: 'Notebook',
        link: '/files/learn-python.ipynb',
      },
      {
        text: 'GitHub',
        link: `https://github.com/${repoOwner}/${repoName}`,
      },
    ],
    sidebar: {
      '/contribution/': contributionSidebar,
      '/': courseSidebar,
    },
    outline: true,
    aside: true,
    footer: {
      message: 'Built with VuePress Theme Plume',
      copyright: 'Copyright © 2026 Meysam Hadeli',
    },
  }),
})

