import argparse
import json
import os

import sympy
from ast_transformer.c.ast_generator import CASTGenerator
from ast_transformer.c.transform_visitor import CTransformVisitor
from ast_transformer.java.ast_generator import JavaASTGenerator
from ast_transformer.java.transform_visitor import JavaTransformVisitor
from ast_transformer.python.ast_generator import PyASTGenerator
from ast_transformer.python.transform_visitor import PyTransformVisitor

from bigo_ast.bigo_ast import FuncDeclNode
from bigo_calculator.bigo_calculator import BigOCalculator
from bigo_calculator.bigo_simplify import BigOSimplify


def main():
    arg_parse = argparse.ArgumentParser(description='A static Big-O analysis tool base on Big-O AST.')
    arg_parse.format_help()
    arg_parse.add_argument('filename', type=str, help='target code filename')

    arg_parse.add_argument('-lang', nargs='?', type=str,
                           help='this argument is optional if file extension is .c or .java')
    # arg_parse.add_argument('-loop', action='store_false', help='calculate loop time complexity.')
    arg_parse.add_argument('-no-simplify', action='store_true', help=' do not simplify time complexity.')

    args = arg_parse.parse_args()

    # check file exist
    source_file_name = args.filename
    if not os.path.isfile(source_file_name):
        raise FileNotFoundError

    json_str = time_calc(source_file_name, file_language = args.lang)
    
    # print function Big-O
    print(json_str)

    return json_str

def time_calc(filename : str, file_language : None):
    # check file exist
    source_file_name = filename
    if not os.path.isfile(source_file_name):
        raise FileNotFoundError

    # default get programming language by extension
    language = os.path.splitext(source_file_name)[1][1:].lower()
    if file_language:
        language = file_language

    # transform ast
    if language == 'c':
        origin_ast = CASTGenerator().generate(source_file_name)
        bigo_ast = CTransformVisitor().transform(origin_ast)
    elif language == 'java':
        origin_ast = JavaASTGenerator().generate(source_file_name)
        bigo_ast = JavaTransformVisitor().transform(origin_ast)
    elif language == 'py':
        origin_ast = PyASTGenerator().generate(source_file_name)
        bigo_ast = PyTransformVisitor().transform(origin_ast)
    else:
        raise Exception("Language does not support : " + language)
    
    # evaluate big o
    BigOCalculator(bigo_ast).calc()
    new_bigo_ast = bigo_ast
    new_bigo_ast = BigOSimplify(bigo_ast).simplify()

    func_bigo_dict = {}
    func_bigo_dict_SympyOrder = {}
    complexity = new_bigo_ast.time_complexity
    func_bigo_dict_SympyOrder.update({'compilation node': complexity})
    if type(complexity) is sympy.Order:
            complexity = str(complexity)
    else:
        complexity = 'O(' + str(complexity) + ')'

    func_bigo_dict.update({'compilation node': complexity})

    for func in new_bigo_ast.children:
        if type(func) != FuncDeclNode:
            continue

        complexity = func.time_complexity

        if func.recursive:
            complexity = 'is a recursive function'
            func_bigo_dict_SympyOrder.update({func.name: sympy.oo})
        elif not complexity:
            raise ArithmeticError('complexity can not recognize.')
        elif type(complexity) is sympy.Order:
            func_bigo_dict_SympyOrder.update({func.name: complexity})
            complexity = str(complexity)
        else:
            func_bigo_dict_SympyOrder.update({func.name: complexity})
            complexity = 'O(' + str(complexity) + ')'

        func_bigo_dict.update({func.name: complexity})

    json_str = json.dumps(func_bigo_dict, indent=4)

    # print function Big-O
    return json_str, func_bigo_dict_SympyOrder

if __name__ == '__main__':
    main()
    # time_calc('examples/colab-py/md1.py')
