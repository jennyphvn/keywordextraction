import turtle
import celtstats as cs
import celtstats.stats as stats
import celtstats.builder as bd
#import my_functions

# to see a help for this package type help('celtstats') in the python interpreter
#documentIndex = {}

def main() :
    values = ['The', 'first', 'time', 'Google', 'Photos', 'made', 'me', 'cry,', 'it', 'was', 'with', 'a', 'sucker', 'punch.', 'I', 'had', 'looked', 'at', 'my', 'phone', 'one', 'morning', 'in', 'April,', 'expecting', 'more', 'news', 'of', 'global', 'woe.', 'Instead', 'there', 'was', 'an', 'alert', 'from', 'Photos,', 'letting', 'me', 'know', 'that', 'Google', 'image-processing', 'robots', 'had', 'created', 'some', 'kind', 'of', 'montage', 'from', 'my', 'videos'
    ]

    numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # invoking the function readFiles defined in the module celtstats.io
    cs.io.readFiles('./texts')

    # invoking the function readFiles defined in the module celtstats.io
    cs.io.writeFile('.', values )

#invoke functions to build dictionary here
    cs.builder.builddict_1()
    print(cs.parser.documentIndex)
    #insert exit(1) to run only the code above it
    #exit(1)
    # invoking the function text2tokens defined in the module celtstats.parser
    print(cs.parser.text2tokens(values))

    # invoking the function avgFoo defined in the module celtstats.stats
    print(cs.stats.avgValue(numbers))

    # using a variable defined in a module in the package
    print(cs.parser.sw)
    print(cs.parser.punctuationMarksList)

    # example of using regular expression to remove some characters
    stringExample = 'this is an 1 2 3 Example 4 5 6 7 8 9 0string to show how to keep only !@#$%^&*()_ - _ = charac\' "t"   ers '

    print('************* Keeps letters and numbers')
    print(cs.parser.useRegularExpression(stringExample))
    print('************* Keeps letters only')
    print(cs.parser.useRegularExpression(stringExample, 'alpha'))
    print('************* Keeps numbers only')
    print(cs.parser.useRegularExpression(stringExample, 'num'))
    print('************* Keeps symbols only')
    print(cs.parser.useRegularExpression(stringExample, 'symb'))
    print('************* Turns to lower case')
    print(cs.parser.useRegularExpression(stringExample, 'lower'))

    # invoking the function drawBar defined in the module celtstats.viz
    cs.viz.drawBar(15, 50, 70, 10, 'blue')

    # add another bar in red
    color = 'red'
    cs.viz.drawBar(35, 50, 70, 10, color)

    # add another bar in yellow
    cs.viz.drawBar(55, 50, 70, 10, 'yellow')

    # add a green bar
    cs.viz.drawBar(75, 50, 70, 10, 'green')

    # the following line should be removed, it's here just for testing purposes
    turtle.exitonclick() # Wait for user's mouse click
#invoke function that reads from files, invokes dictionary
main()

# Notes about packages
# Regular packages are self-contained: all parts live in the same directory hierarchy.
