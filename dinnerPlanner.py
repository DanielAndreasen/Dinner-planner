#!/usr/bin/env python
# -*- coding: utf8 -*-

# My imports
import argparse
import yaml


def _parser():
    p = argparse.ArgumentParser(description='What to choose for dinner')
    p.add_argument('-f', '--frequency', choices='d w m'.split(), default='d',
                   help='You want a planner daily, weekly or monthly')
    p.add_argument('-i', '--ingredients', nargs='+', default=False,
                   help='List the ingredients here (space seperated)')
    return p.parse_args()


def _print_ingredients(ingredients):
    N = len(ingredients)
    s0 = 'You will need '
    s1 = '{}, ' * (N - 1)
    s2 = 'and {}'
    s = '%s%s%s' % (s0, s1, s2)
    return s.format(*ingredients)


def main(frequency=False, ingredients=False):
    freq = {'d': 1, 'w': 7, 'm': 30}
    with open('recipies.yml', 'r') as f:
        recipies = yaml.safe_load(f)

    for k, v in recipies.iteritems():
        recipies[k] = v.split()
        if ingredients:
            counter = 0
            for ingredient in ingredients:
                if ingredient.lower() in v.lower():
                    counter += 1
            recipies[k].append(counter)

    if ingredients:
        recipies = sorted(recipies.iteritems(), key=lambda (k, v): v[-1], reverse=True)
        for i, recipie in enumerate(recipies):
            if i > 1:
                break
            ingredient_list = recipie[1][:-1]
            print '\nLet me recommend "%s"' % recipie[0]
            print _print_ingredients(ingredient_list)




if __name__ == '__main__':
    p = _parser()
    if p.ingredients and p.frequency in 'wm':
        print 'Using the ingredient list only for 1 day'
        p.frequency = False
    main(p.frequency, p.ingredients)
