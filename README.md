# Testing in Python

Via https://martinfowler.com/articles/practical-test-pyramid.html

1. Static tests
1. Unit tests
1. Service tests
1. Integration tests

## Static tests

### Formatting

Wasn't used to formatting when writing C#, since only a single IDE was used (the IDE written by the creators of the language). Thus resulting in the same format of code for the whole team.
In Python this is different, the language is more free and there isn't a go-to IDE. In my team both VS Code and PyCharm were used, resulting in different formats.
I prefer VS Code since it's lightweight, easy to configure and can be used for a lot of programming languages.
Formatters are nice to prevent changes which aren't actually changes in merge requests. One formatter could add a whitespace somewhere, while the other one removes. In merge requests, depending on the person's formatter, this might change everytime while what the code does doesn't change. From my experience [black](https://pypi.org/project/black/) is the best, since it just works out of the box without any configuration and is supported in both VS Code and PyCharm.

### Linting

Linting not part of tests, but improves the code quality.
Linters:

. mypy: checks typing, which is nice since Python doesn't this out of the box (use `--strict`)
. prospector: many usefull hints, but can be a bit too many
. pydocstyle: forces documentation, could be nice, although it forces you to also write documentation for methods which are self explanatory

## Unit tests

Level: class
Use only for isolated, complex logic.
Cost relatively a lot of time to write for all classes.
Aren't always realistic, thus can be misleading. If a class is fully covered with tests it might seem good, but if some of the methods are never called by another class the code can be removed. Thus code coverage can't be used to see which code is actually used and which isn't.

## Service tests

Level: (micro)service
Test the code in a realistic situation.
Preferably using feature files. Allows to focus on the functional use of the code. Makes is readable for non technical people and also yourself and the team if you haven't looked at them for some time. If I look at unit tests which I or a teammate has written a few months ago, it's sometimes hard to see what it tries to test.
Mock only at the end of the service at the interface with another service. This could be a database call or call to another microservice. This allows testing of the whole code of the service via realistic scenario's. Here code coverage can be useful. If you your scenario's properly cover all realistic scenario's, code which isn't covered doesn't do anything and could be removed.

## Integration tests

Level: whole landscape
Also called end to end tests or smoke tests, their definition is a bit different but their goal is the same: test a new version of a service within the whole landscape. In the previous level of tests a change could pass all tests within the service, but it could cause a failure in another microservice with which it communicates. Integration tests don't mock services, but are run in a production-like environment. They will often prepare a state in the environment, for example injecting the right records into a database, and than do a call at the interface of the landscape. After this call is processed in all services the response can be checked, but also the state of the rest of the environment. The call should have resulted in an additional record in a database for example or a message being put in a queue.
Of course features files also work for this

## Types of testing

### Assert tests

Either in code or via feature files

### Property based tests

Or just fuzzing

### Mutation testing

Interesting, but hard to use in an automated way. Can be useful if used in the right way.