# Contributing

Please read [14 Ways to Contribute to Open Source without Being a Programming Genius or a Rock Star](https://smartbear.com/blog/14-ways-to-contribute-to-open-source-without-being/)

## Workflow

I like the [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).

The mentioned links from Atlassian are the recommended docs to read and
understand the git workflows.

## Git Commit

The cardinal rule for creating good commits is to ensure there is only one
"logical change" per commit.

Things to avoid when creating commits

-   Mixing whitespace changes with functional code changes.
-   Mixing two unrelated functional changes.
-   Sending large new features in a single giant commit.

## Git Commit Conventions

I use git commit as per [Conventional Changelog](https://github.com/ajoslin/conventional-changelog):

```text
<type>(<scope>): <subject>
```

Example:

```text
docs(CONTRIBUTING.md): add commit message guidelines
feat(backend): add user authentication
```

### Allowed types:

-   **feat**: A new feature
-   **fix**: A bug fix
-   **docs**: Documentation only changes
-   **style**: Changes that do not affect the meaning of the code (white-space,
    formatting, missing semi-colons, etc)
-   **refactor**: A code change that neither fixes a bug or adds a feature
-   **perf**: A code change that improves performance
-   **test**: Adding missing tests
-   **chore**: Changes to the build process or auxiliary tools and libraries such
    as documentation generation