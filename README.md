# Testing in Python

Testing is something which the more I program, the more I appreciate and learn about. Consequently this also leads to more discussions with teammates and other developers about what the best way is to write tests. I think having tests is almost always better than having no tests, even if they are just simple unit tests for only the happy flow. But there are plenty ways to test your code. So in my opinion you can write good tests and you can write better tests.

## Importance of tests

Tests are an essential part about software developing and as I said I appreciate them more and more, but why are they important? So from my experience this comes down to the following:

- They describe what the code should do. So without diving into the code, which someone else could have written, I can still understand what the code does.
- I can make changes to code without breaking anything, because tests give me certainty that everything still works as expected.
- Automated tests can be run in a pipeline, which gives me feedback about whether my code works in a real environment. If a test fails on an environment, the failed test tells me a direction where something is broken which allows me to fix it quickly.

## Types of tests

Often when people talk about testing one of the first things that comes up if the test pyramid. In [this article](https://martinfowler.com/articles/practical-test-pyramid.html) the following things can be taken away about the pyramid:

- If tests get more integrated they also get slower
- Write tests with different granularity
- The more high-level you get the fewer tests you should have

Although I agree with the first and second point, I don't totally agree with the third point. I think the higher the tests are integrated, the more valuable the tests are. There are also some other reasons, which I'll tell about when walking past the different types of tests. In every test pyramid the names of the levels are slightly different, but I think the level of integration of a test is more important than the name. So I'll be using the following levels:

1. Static tests
1. Unit tests
1. Service tests
1. Smoke tests

## 1. Static tests

Static tests are tests where the code isn't run, but just the static code is analyzed in comparison to the other levels where the code is actually run. Although static testing often isn't part of the test pyramid, I still think it has some value. There are many different static tests, but for Python I think linting is the most important one. Since Python allows for [dynamic typing](https://realpython.com/python-type-checking/#dynamic-typing) and there is no go to editor (I prefer VS Code of course), this can lead to interesting code. I learned that you can use multiple linters as long as they don't focus on the same thing. In the next paragraphs I'll be talking about the different linters for Python that I think have value.

There are many linters which can be used to format your code. It's hard to say which one is the best, but I prefer [Black](https://github.com/psf/black). The goal of Black is to have (nearly) no configuration for your linter, preventing discussions about the formatting of code. On a project I used to have discussions about this with another teammate, while Black would take away these dicussions.

The linter [mypy](http://mypy-lang.org/) checks typing in Python. Before I programmed Python, I used to program in C# where typing was necessary. When I started with Python I created the habit to not use typing anymore, since it wasn't enforced. Although at first this made things easier, later on I noticed it made the quality of the code more poor.

The linter [prospector](http://prospector.landscape.io/en/master/) gives many usefull hints about improvements of the code, like unused variables. Although the hints are nice, they can be a bit too much. So far I haven't actually enforced prospector on a project, but I have just been using hints from prospector.

The linter [pydocstyle](https://github.com/PyCQA/pydocstyle/) forces documentation for methods and classes. This could be nice, although it forces you to also write documentation for methods which are self explanatory. I think this would depend on the type of the project, if the logic is difficult or the domain complex, enforcing documentation with pydocstyle could be nice.

## 2. Unit tests

Level: class
Use only for isolated, complex logic.
Cost relatively a lot of time to write for all classes.
Aren't always realistic, thus can be misleading. If a class is fully covered with tests it might seem good, but if some of the methods are never called by another class the code can be removed. Thus code coverage can't be used to see which code is actually used and which isn't.

### Assert tests

Either in code or via feature files

### Property based tests

Or just fuzzing

### Mutation testing

Interesting, but hard to use in an automated way. Can be useful if used in the right way.

## 3. Service tests

Level: (micro)service
Test the code in a realistic situation.
Preferably using feature files. Allows to focus on the functional use of the code. Makes is readable for non technical people and also yourself and the team if you haven't looked at them for some time. If I look at unit tests which I or a teammate has written a few months ago, it's sometimes hard to see what it tries to test.
Mock only at the end of the service at the interface with another service. This could be a database call or call to another microservice. This allows testing of the whole code of the service via realistic scenario's. Here code coverage can be useful. If you your scenario's properly cover all realistic scenario's, code which isn't covered doesn't do anything and could be removed.

## 4. Integration tests

Level: whole landscape
Also called end to end tests or smoke tests, their definition is a bit different but their goal is the same: test a new version of a service within the whole landscape. In the previous level of tests a change could pass all tests within the service, but it could cause a failure in another microservice with which it communicates. Integration tests don't mock services, but are run in a production-like environment. They will often prepare a state in the environment, for example injecting the right records into a database, and than do a call at the interface of the landscape. After this call is processed in all services the response can be checked, but also the state of the rest of the environment. The call should have resulted in an additional record in a database for example or a message being put in a queue.
Of course features files also work for this
