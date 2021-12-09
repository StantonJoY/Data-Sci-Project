Module(
    body=[
        Expr(
            value=Constant(value='\nsafe_eval module - methods intended to provide more restricted alternatives to\n                   evaluate simple and/or untrusted code.\n\nMethods in this module are typically used as alternatives to eval() to parse\nOpenERP domain strings, conditions and expressions, mostly based on locals\ncondition/math builtins.\n', kind=None),
        ),
        Import(
            names=[alias(name='dis', asname=None)],
        ),
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='types', asname=None)],
        ),
        ImportFrom(
            module='opcode',
            names=[
                alias(name='HAVE_ARGUMENT', asname=None),
                alias(name='opmap', asname=None),
                alias(name='opname', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='types',
            names=[alias(name='CodeType', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='OperationalError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='misc',
            names=[alias(name='ustr', asname=None)],
            level=1,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Assign(
            targets=[Name(id='unsafe_eval', ctx=Store())],
            value=Name(id='eval', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='__all__', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='test_expr', kind=None),
                    Constant(value='safe_eval', kind=None),
                    Constant(value='const_eval', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_ALLOWED_MODULES', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='_strptime', kind=None),
                    Constant(value='math', kind=None),
                    Constant(value='time', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_UNSAFE_ATTRIBUTES', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='f_builtins', kind=None),
                    Constant(value='f_globals', kind=None),
                    Constant(value='f_locals', kind=None),
                    Constant(value='gi_frame', kind=None),
                    Constant(value='co_code', kind=None),
                    Constant(value='func_globals', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='to_opcodes',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='opnames', annotation=None, type_comment=None),
                    arg(arg='_opmap', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Name(id='opmap', ctx=Load())],
            ),
            body=[
                For(
                    target=Name(id='x', ctx=Store()),
                    iter=Name(id='opnames', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='x', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='_opmap', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Subscript(
                                            value=Name(id='_opmap', ctx=Load()),
                                            slice=Name(id='x', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_BLACKLIST', ctx=Store())],
            value=Call(
                func=Name(id='set', ctx=Load()),
                args=[
                    Call(
                        func=Name(id='to_opcodes', ctx=Load()),
                        args=[
                            List(
                                elts=[
                                    Constant(value='IMPORT_STAR', kind=None),
                                    Constant(value='IMPORT_NAME', kind=None),
                                    Constant(value='IMPORT_FROM', kind=None),
                                    Constant(value='STORE_ATTR', kind=None),
                                    Constant(value='DELETE_ATTR', kind=None),
                                    Constant(value='STORE_GLOBAL', kind=None),
                                    Constant(value='DELETE_GLOBAL', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_CONST_OPCODES', ctx=Store())],
            value=BinOp(
                left=Call(
                    func=Name(id='set', ctx=Load()),
                    args=[
                        Call(
                            func=Name(id='to_opcodes', ctx=Load()),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='POP_TOP', kind=None),
                                        Constant(value='ROT_TWO', kind=None),
                                        Constant(value='ROT_THREE', kind=None),
                                        Constant(value='ROT_FOUR', kind=None),
                                        Constant(value='DUP_TOP', kind=None),
                                        Constant(value='DUP_TOP_TWO', kind=None),
                                        Constant(value='LOAD_CONST', kind=None),
                                        Constant(value='RETURN_VALUE', kind=None),
                                        Constant(value='BUILD_LIST', kind=None),
                                        Constant(value='BUILD_MAP', kind=None),
                                        Constant(value='BUILD_TUPLE', kind=None),
                                        Constant(value='BUILD_SET', kind=None),
                                        Constant(value='BUILD_CONST_KEY_MAP', kind=None),
                                        Constant(value='LIST_EXTEND', kind=None),
                                        Constant(value='SET_UPDATE', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                op=Sub(),
                right=Name(id='_BLACKLIST', ctx=Load()),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_operations', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='POWER', kind=None),
                    Constant(value='MULTIPLY', kind=None),
                    Constant(value='FLOOR_DIVIDE', kind=None),
                    Constant(value='TRUE_DIVIDE', kind=None),
                    Constant(value='MODULO', kind=None),
                    Constant(value='ADD', kind=None),
                    Constant(value='SUBTRACT', kind=None),
                    Constant(value='LSHIFT', kind=None),
                    Constant(value='RSHIFT', kind=None),
                    Constant(value='AND', kind=None),
                    Constant(value='XOR', kind=None),
                    Constant(value='OR', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_EXPR_OPCODES', ctx=Store())],
            value=BinOp(
                left=Call(
                    func=Attribute(
                        value=Name(id='_CONST_OPCODES', ctx=Load()),
                        attr='union',
                        ctx=Load(),
                    ),
                    args=[
                        Call(
                            func=Name(id='to_opcodes', ctx=Load()),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='UNARY_POSITIVE', kind=None),
                                        Constant(value='UNARY_NEGATIVE', kind=None),
                                        Constant(value='UNARY_NOT', kind=None),
                                        Constant(value='UNARY_INVERT', kind=None),
                                        Starred(
                                            value=GeneratorExp(
                                                elt=BinOp(
                                                    left=Constant(value='BINARY_', kind=None),
                                                    op=Add(),
                                                    right=Name(id='op', ctx=Load()),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='op', ctx=Store()),
                                                        iter=Name(id='_operations', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            ctx=Load(),
                                        ),
                                        Constant(value='BINARY_SUBSCR', kind=None),
                                        Starred(
                                            value=GeneratorExp(
                                                elt=BinOp(
                                                    left=Constant(value='INPLACE_', kind=None),
                                                    op=Add(),
                                                    right=Name(id='op', ctx=Load()),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='op', ctx=Store()),
                                                        iter=Name(id='_operations', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            ctx=Load(),
                                        ),
                                        Constant(value='BUILD_SLICE', kind=None),
                                        Constant(value='LIST_APPEND', kind=None),
                                        Constant(value='MAP_ADD', kind=None),
                                        Constant(value='SET_ADD', kind=None),
                                        Constant(value='COMPARE_OP', kind=None),
                                        Constant(value='IS_OP', kind=None),
                                        Constant(value='CONTAINS_OP', kind=None),
                                        Constant(value='DICT_MERGE', kind=None),
                                        Constant(value='DICT_UPDATE', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                op=Sub(),
                right=Name(id='_BLACKLIST', ctx=Load()),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_SAFE_OPCODES', ctx=Store())],
            value=BinOp(
                left=Call(
                    func=Attribute(
                        value=Name(id='_EXPR_OPCODES', ctx=Load()),
                        attr='union',
                        ctx=Load(),
                    ),
                    args=[
                        Call(
                            func=Name(id='to_opcodes', ctx=Load()),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='POP_BLOCK', kind=None),
                                        Constant(value='POP_EXCEPT', kind=None),
                                        Constant(value='SETUP_LOOP', kind=None),
                                        Constant(value='SETUP_EXCEPT', kind=None),
                                        Constant(value='BREAK_LOOP', kind=None),
                                        Constant(value='CONTINUE_LOOP', kind=None),
                                        Constant(value='EXTENDED_ARG', kind=None),
                                        Constant(value='MAKE_FUNCTION', kind=None),
                                        Constant(value='CALL_FUNCTION', kind=None),
                                        Constant(value='CALL_FUNCTION_KW', kind=None),
                                        Constant(value='CALL_FUNCTION_EX', kind=None),
                                        Constant(value='CALL_METHOD', kind=None),
                                        Constant(value='LOAD_METHOD', kind=None),
                                        Constant(value='GET_ITER', kind=None),
                                        Constant(value='FOR_ITER', kind=None),
                                        Constant(value='YIELD_VALUE', kind=None),
                                        Constant(value='JUMP_FORWARD', kind=None),
                                        Constant(value='JUMP_ABSOLUTE', kind=None),
                                        Constant(value='JUMP_IF_FALSE_OR_POP', kind=None),
                                        Constant(value='JUMP_IF_TRUE_OR_POP', kind=None),
                                        Constant(value='POP_JUMP_IF_FALSE', kind=None),
                                        Constant(value='POP_JUMP_IF_TRUE', kind=None),
                                        Constant(value='SETUP_FINALLY', kind=None),
                                        Constant(value='END_FINALLY', kind=None),
                                        Constant(value='BEGIN_FINALLY', kind=None),
                                        Constant(value='CALL_FINALLY', kind=None),
                                        Constant(value='POP_FINALLY', kind=None),
                                        Constant(value='RAISE_VARARGS', kind=None),
                                        Constant(value='LOAD_NAME', kind=None),
                                        Constant(value='STORE_NAME', kind=None),
                                        Constant(value='DELETE_NAME', kind=None),
                                        Constant(value='LOAD_ATTR', kind=None),
                                        Constant(value='LOAD_FAST', kind=None),
                                        Constant(value='STORE_FAST', kind=None),
                                        Constant(value='DELETE_FAST', kind=None),
                                        Constant(value='UNPACK_SEQUENCE', kind=None),
                                        Constant(value='STORE_SUBSCR', kind=None),
                                        Constant(value='LOAD_GLOBAL', kind=None),
                                        Constant(value='RERAISE', kind=None),
                                        Constant(value='JUMP_IF_NOT_EXC_MATCH', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                op=Sub(),
                right=Name(id='_BLACKLIST', ctx=Load()),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='assert_no_dunder_name',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='code_obj', annotation=None, type_comment=None),
                    arg(arg='expr', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' assert_no_dunder_name(code_obj, expr) -> None\n\n    Asserts that the code object does not refer to any "dunder name"\n    (__$name__), so that safe_eval prevents access to any internal-ish Python\n    attribute or method (both are loaded via LOAD_ATTR which uses a name, not a\n    const or a var).\n\n    Checks that no such name exists in the provided code object (co_names).\n\n    :param code_obj: code object to name-validate\n    :type code_obj: CodeType\n    :param str expr: expression corresponding to the code object, for debugging\n                     purposes\n    :raises NameError: in case a forbidden name (containing two underscores)\n                       is found in ``code_obj``\n\n    .. note:: actually forbids every name containing 2 underscores\n    ', kind=None),
                ),
                For(
                    target=Name(id='name', ctx=Store()),
                    iter=Attribute(
                        value=Name(id='code_obj', ctx=Load()),
                        attr='co_names',
                        ctx=Load(),
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='__', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='name', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Name(id='name', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='_UNSAFE_ATTRIBUTES', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='NameError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Access to forbidden name %r (%r)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='name', ctx=Load()),
                                                        Name(id='expr', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='assert_valid_codeobj',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='allowed_codes', annotation=None, type_comment=None),
                    arg(arg='code_obj', annotation=None, type_comment=None),
                    arg(arg='expr', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Asserts that the provided code object validates against the bytecode\n    and name constraints.\n\n    Recursively validates the code objects stored in its co_consts in case\n    lambdas are being created/used (lambdas generate their own separated code\n    objects and don't live in the root one)\n\n    :param allowed_codes: list of permissible bytecode instructions\n    :type allowed_codes: set(int)\n    :param code_obj: code object to name-validate\n    :type code_obj: CodeType\n    :param str expr: expression corresponding to the code object, for debugging\n                     purposes\n    :raises ValueError: in case of forbidden bytecode in ``code_obj``\n    :raises NameError: in case a forbidden name (containing two underscores)\n                       is found in ``code_obj``\n    ", kind=None),
                ),
                Expr(
                    value=Call(
                        func=Name(id='assert_no_dunder_name', ctx=Load()),
                        args=[
                            Name(id='code_obj', ctx=Load()),
                            Name(id='expr', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='code_codes', ctx=Store())],
                    value=SetComp(
                        elt=Attribute(
                            value=Name(id='i', ctx=Load()),
                            attr='opcode',
                            ctx=Load(),
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='i', ctx=Store()),
                                iter=Call(
                                    func=Attribute(
                                        value=Name(id='dis', ctx=Load()),
                                        attr='get_instructions',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='code_obj', ctx=Load())],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Compare(
                            left=Name(id='allowed_codes', ctx=Load()),
                            ops=[GtE()],
                            comparators=[Name(id='code_codes', ctx=Load())],
                        ),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='forbidden opcode(s) in %r: %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='expr', ctx=Load()),
                                                Call(
                                                    func=Attribute(
                                                        value=Constant(value=', ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=Subscript(
                                                                value=Name(id='opname', ctx=Load()),
                                                                slice=Name(id='x', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='x', ctx=Store()),
                                                                    iter=BinOp(
                                                                        left=Name(id='code_codes', ctx=Load()),
                                                                        op=Sub(),
                                                                        right=Name(id='allowed_codes', ctx=Load()),
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                For(
                    target=Name(id='const', ctx=Store()),
                    iter=Attribute(
                        value=Name(id='code_obj', ctx=Load()),
                        attr='co_consts',
                        ctx=Load(),
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='const', ctx=Load()),
                                    Name(id='CodeType', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='assert_valid_codeobj', ctx=Load()),
                                        args=[
                                            Name(id='allowed_codes', ctx=Load()),
                                            Name(id='const', ctx=Load()),
                                            Constant(value='lambda', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='test_expr',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='expr', annotation=None, type_comment=None),
                    arg(arg='allowed_codes', annotation=None, type_comment=None),
                    arg(arg='mode', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='eval', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='test_expr(expression, allowed_codes[, mode]) -> code_object\n\n    Test that the expression contains only the allowed opcodes.\n    If the expression is valid and contains only allowed codes,\n    return the compiled code object.\n    Otherwise raise a ValueError, a Syntax Error or TypeError accordingly.\n    ', kind=None),
                ),
                Try(
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='mode', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='eval', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='expr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expr', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='code_obj', ctx=Store())],
                            value=Call(
                                func=Name(id='compile', ctx=Load()),
                                args=[
                                    Name(id='expr', ctx=Load()),
                                    Constant(value='', kind=None),
                                    Name(id='mode', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Tuple(
                                elts=[
                                    Name(id='SyntaxError', ctx=Load()),
                                    Name(id='TypeError', ctx=Load()),
                                    Name(id='ValueError', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            name=None,
                            body=[Raise(exc=None, cause=None)],
                        ),
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='e',
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='"%s" while compiling\n%r', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='ustr', ctx=Load()),
                                                            args=[Name(id='e', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Name(id='expr', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Expr(
                    value=Call(
                        func=Name(id='assert_valid_codeobj', ctx=Load()),
                        args=[
                            Name(id='allowed_codes', ctx=Load()),
                            Name(id='code_obj', ctx=Load()),
                            Name(id='expr', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Name(id='code_obj', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='const_eval',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='expr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='const_eval(expression) -> value\n\n    Safe Python constant evaluation\n\n    Evaluates a string that contains an expression describing\n    a Python constant. Strings that are not valid Python expressions\n    or that contain other code besides the constant raise ValueError.\n\n    >>> const_eval("10")\n    10\n    >>> const_eval("[1,2, (3,4), {\'foo\':\'bar\'}]")\n    [1, 2, (3, 4), {\'foo\': \'bar\'}]\n    >>> const_eval("1+2")\n    Traceback (most recent call last):\n    ...\n    ValueError: opcode BINARY_ADD not allowed\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='c', ctx=Store())],
                    value=Call(
                        func=Name(id='test_expr', ctx=Load()),
                        args=[
                            Name(id='expr', ctx=Load()),
                            Name(id='_CONST_OPCODES', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='unsafe_eval', ctx=Load()),
                        args=[Name(id='c', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='expr_eval',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='expr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='expr_eval(expression) -> value\n\n    Restricted Python expression evaluation\n\n    Evaluates a string that contains an expression that only\n    uses Python constants. This can be used to e.g. evaluate\n    a numerical expression from an untrusted source.\n\n    >>> expr_eval("1+2")\n    3\n    >>> expr_eval("[1,2]*2")\n    [1, 2, 1, 2]\n    >>> expr_eval("__import__(\'sys\').modules")\n    Traceback (most recent call last):\n    ...\n    ValueError: opcode LOAD_NAME not allowed\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='c', ctx=Store())],
                    value=Call(
                        func=Name(id='test_expr', ctx=Load()),
                        args=[
                            Name(id='expr', ctx=Load()),
                            Name(id='_EXPR_OPCODES', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='unsafe_eval', ctx=Load()),
                        args=[Name(id='c', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_import',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='name', annotation=None, type_comment=None),
                    arg(arg='globals', annotation=None, type_comment=None),
                    arg(arg='locals', annotation=None, type_comment=None),
                    arg(arg='fromlist', annotation=None, type_comment=None),
                    arg(arg='level', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    UnaryOp(
                        op=USub(),
                        operand=Constant(value=1, kind=None),
                    ),
                ],
            ),
            body=[
                If(
                    test=Compare(
                        left=Name(id='globals', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='globals', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='locals', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='locals', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='fromlist', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fromlist', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='name', ctx=Load()),
                        ops=[In()],
                        comparators=[Name(id='_ALLOWED_MODULES', ctx=Load())],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='__import__', ctx=Load()),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='globals', ctx=Load()),
                                    Name(id='locals', ctx=Load()),
                                    Name(id='level', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Raise(
                    exc=Call(
                        func=Name(id='ImportError', ctx=Load()),
                        args=[Name(id='name', ctx=Load())],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_BUILTINS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='__import__', kind=None),
                    Constant(value='True', kind=None),
                    Constant(value='False', kind=None),
                    Constant(value='None', kind=None),
                    Constant(value='bytes', kind=None),
                    Constant(value='str', kind=None),
                    Constant(value='unicode', kind=None),
                    Constant(value='bool', kind=None),
                    Constant(value='int', kind=None),
                    Constant(value='float', kind=None),
                    Constant(value='enumerate', kind=None),
                    Constant(value='dict', kind=None),
                    Constant(value='list', kind=None),
                    Constant(value='tuple', kind=None),
                    Constant(value='map', kind=None),
                    Constant(value='abs', kind=None),
                    Constant(value='min', kind=None),
                    Constant(value='max', kind=None),
                    Constant(value='sum', kind=None),
                    Constant(value='reduce', kind=None),
                    Constant(value='filter', kind=None),
                    Constant(value='sorted', kind=None),
                    Constant(value='round', kind=None),
                    Constant(value='len', kind=None),
                    Constant(value='repr', kind=None),
                    Constant(value='set', kind=None),
                    Constant(value='all', kind=None),
                    Constant(value='any', kind=None),
                    Constant(value='ord', kind=None),
                    Constant(value='chr', kind=None),
                    Constant(value='divmod', kind=None),
                    Constant(value='isinstance', kind=None),
                    Constant(value='range', kind=None),
                    Constant(value='xrange', kind=None),
                    Constant(value='zip', kind=None),
                    Constant(value='Exception', kind=None),
                ],
                values=[
                    Name(id='_import', ctx=Load()),
                    Constant(value=True, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=None, kind=None),
                    Name(id='bytes', ctx=Load()),
                    Name(id='str', ctx=Load()),
                    Name(id='str', ctx=Load()),
                    Name(id='bool', ctx=Load()),
                    Name(id='int', ctx=Load()),
                    Name(id='float', ctx=Load()),
                    Name(id='enumerate', ctx=Load()),
                    Name(id='dict', ctx=Load()),
                    Name(id='list', ctx=Load()),
                    Name(id='tuple', ctx=Load()),
                    Name(id='map', ctx=Load()),
                    Name(id='abs', ctx=Load()),
                    Name(id='min', ctx=Load()),
                    Name(id='max', ctx=Load()),
                    Name(id='sum', ctx=Load()),
                    Attribute(
                        value=Name(id='functools', ctx=Load()),
                        attr='reduce',
                        ctx=Load(),
                    ),
                    Name(id='filter', ctx=Load()),
                    Name(id='sorted', ctx=Load()),
                    Name(id='round', ctx=Load()),
                    Name(id='len', ctx=Load()),
                    Name(id='repr', ctx=Load()),
                    Name(id='set', ctx=Load()),
                    Name(id='all', ctx=Load()),
                    Name(id='any', ctx=Load()),
                    Name(id='ord', ctx=Load()),
                    Name(id='chr', ctx=Load()),
                    Name(id='divmod', ctx=Load()),
                    Name(id='isinstance', ctx=Load()),
                    Name(id='range', ctx=Load()),
                    Name(id='range', ctx=Load()),
                    Name(id='zip', ctx=Load()),
                    Name(id='Exception', ctx=Load()),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='safe_eval',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='expr', annotation=None, type_comment=None),
                    arg(arg='globals_dict', annotation=None, type_comment=None),
                    arg(arg='locals_dict', annotation=None, type_comment=None),
                    arg(arg='mode', annotation=None, type_comment=None),
                    arg(arg='nocopy', annotation=None, type_comment=None),
                    arg(arg='locals_builtins', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value='eval', kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='safe_eval(expression[, globals[, locals[, mode[, nocopy]]]]) -> result\n\n    System-restricted Python expression evaluation\n\n    Evaluates a string that contains an expression that mostly\n    uses Python constants, arithmetic expressions and the\n    objects directly provided in context.\n\n    This can be used to e.g. evaluate\n    an OpenERP domain expression from an untrusted source.\n\n    :throws TypeError: If the expression provided is a code object\n    :throws SyntaxError: If the expression provided is not valid Python\n    :throws NameError: If the expression provided accesses forbidden names\n    :throws ValueError: If the expression provided uses forbidden bytecode\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='type', ctx=Load()),
                            args=[Name(id='expr', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Is()],
                        comparators=[Name(id='CodeType', ctx=Load())],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='TypeError', ctx=Load()),
                                args=[Constant(value='safe_eval does not allow direct evaluation of code objects.', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='nocopy', ctx=Load()),
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='globals_dict', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='type', ctx=Load()),
                                                    args=[Name(id='globals_dict', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Name(id='dict', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='locals_dict', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='type', ctx=Load()),
                                                    args=[Name(id='locals_dict', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Name(id='dict', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Looks like you are trying to pass a dynamic environment, you should probably pass nocopy=True to safe_eval().', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='globals_dict', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='globals_dict', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='globals_dict', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='locals_dict', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='locals_dict', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='locals_dict', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Name(id='check_values', ctx=Load()),
                        args=[Name(id='globals_dict', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='check_values', ctx=Load()),
                        args=[Name(id='locals_dict', ctx=Load())],
                        keywords=[],
                    ),
                ),
                If(
                    test=Compare(
                        left=Name(id='globals_dict', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='globals_dict', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[
                        Subscript(
                            value=Name(id='globals_dict', ctx=Load()),
                            slice=Constant(value='__builtins__', kind=None),
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='_BUILTINS', ctx=Load()),
                    type_comment=None,
                ),
                If(
                    test=Name(id='locals_builtins', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='locals_dict', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='locals_dict', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='locals_dict', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='_BUILTINS', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='c', ctx=Store())],
                    value=Call(
                        func=Name(id='test_expr', ctx=Load()),
                        args=[
                            Name(id='expr', ctx=Load()),
                            Name(id='_SAFE_OPCODES', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='mode',
                                value=Name(id='mode', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='unsafe_eval', ctx=Load()),
                                args=[
                                    Name(id='c', ctx=Load()),
                                    Name(id='globals_dict', ctx=Load()),
                                    Name(id='locals_dict', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='exceptions',
                                    ctx=Load(),
                                ),
                                attr='UserError',
                                ctx=Load(),
                            ),
                            name=None,
                            body=[Raise(exc=None, cause=None)],
                        ),
                        ExceptHandler(
                            type=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='exceptions',
                                    ctx=Load(),
                                ),
                                attr='RedirectWarning',
                                ctx=Load(),
                            ),
                            name=None,
                            body=[Raise(exc=None, cause=None)],
                        ),
                        ExceptHandler(
                            type=Attribute(
                                value=Attribute(
                                    value=Name(id='werkzeug', ctx=Load()),
                                    attr='exceptions',
                                    ctx=Load(),
                                ),
                                attr='HTTPException',
                                ctx=Load(),
                            ),
                            name=None,
                            body=[Raise(exc=None, cause=None)],
                        ),
                        ExceptHandler(
                            type=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='http',
                                    ctx=Load(),
                                ),
                                attr='AuthenticationError',
                                ctx=Load(),
                            ),
                            name=None,
                            body=[Raise(exc=None, cause=None)],
                        ),
                        ExceptHandler(
                            type=Name(id='OperationalError', ctx=Load()),
                            name=None,
                            body=[Raise(exc=None, cause=None)],
                        ),
                        ExceptHandler(
                            type=Name(id='ZeroDivisionError', ctx=Load()),
                            name=None,
                            body=[Raise(exc=None, cause=None)],
                        ),
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='e',
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s: "%s" while evaluating\n%r', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='ustr', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='type', ctx=Load()),
                                                                    args=[Name(id='e', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Name(id='ustr', ctx=Load()),
                                                            args=[Name(id='e', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Name(id='expr', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='test_python_expr',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='expr', annotation=None, type_comment=None),
                    arg(arg='mode', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='eval', kind=None)],
            ),
            body=[
                Try(
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='test_expr', ctx=Load()),
                                args=[
                                    Name(id='expr', ctx=Load()),
                                    Name(id='_SAFE_OPCODES', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Name(id='mode', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Tuple(
                                elts=[
                                    Name(id='SyntaxError', ctx=Load()),
                                    Name(id='TypeError', ctx=Load()),
                                    Name(id='ValueError', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            name='err',
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='err', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[GtE()],
                                                comparators=[Constant(value=2, kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='err', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[GtE()],
                                                comparators=[Constant(value=4, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='error', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='message', kind=None),
                                                    Constant(value='filename', kind=None),
                                                    Constant(value='lineno', kind=None),
                                                    Constant(value='offset', kind=None),
                                                    Constant(value='error_line', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='err', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='err', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='err', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='err', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='err', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=3, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s : %s at line %d\n%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Call(
                                                                func=Name(id='type', ctx=Load()),
                                                                args=[Name(id='err', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='__name__',
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='message', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='lineno', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='error_line', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='ustr', ctx=Load()),
                                                args=[Name(id='err', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Return(
                                    value=Name(id='msg', ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Return(
                    value=Constant(value=False, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='check_values',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='d', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='d', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Name(id='d', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                For(
                    target=Name(id='v', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='d', ctx=Load()),
                            attr='values',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='v', ctx=Load()),
                                    Attribute(
                                        value=Name(id='types', ctx=Load()),
                                        attr='ModuleType',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='TypeError', ctx=Load()),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='Module ', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='v', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' can not be used in evaluation contexts\n\nPrefer providing only the items necessary for your intended use.\n\nIf a "module" is necessary for backwards compatibility, use\n`odoo.tools.safe_eval.wrap_module` to generate a wrapper recursively\nwhitelisting allowed attributes.\n\nPre-wrapped modules are provided as attributes of `odoo.tools.safe_eval`.\n', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='d', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='wrap_module',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                            arg(arg='attributes', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Helper for wrapping a package/module to expose selected attributes\n\n        :param module: the actual package/module to wrap, as returned by ``import <module>``\n        :param iterable attributes: attributes to expose / whitelist. If a dict,\n                                    the keys are the attributes and the values\n                                    are used as an ``attributes`` in case the\n                                    corresponding item is a submodule\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='modfile', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='module', ctx=Load()),
                                    Constant(value='__file__', kind=None),
                                    Constant(value='(built-in)', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_repr',
                                    ctx=Store(),
                                ),
                            ],
                            value=JoinedStr(
                                values=[
                                    Constant(value='<wrapped ', kind=None),
                                    FormattedValue(
                                        value=Attribute(
                                            value=Name(id='module', ctx=Load()),
                                            attr='__name__',
                                            ctx=Load(),
                                        ),
                                        conversion=114,
                                        format_spec=None,
                                    ),
                                    Constant(value=' (', kind=None),
                                    FormattedValue(
                                        value=Name(id='modfile', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=')>', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attrib', ctx=Store()),
                            iter=Name(id='attributes', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='target', ctx=Store())],
                                    value=Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='module', ctx=Load()),
                                            Name(id='attrib', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='target', ctx=Load()),
                                            Attribute(
                                                value=Name(id='types', ctx=Load()),
                                                attr='ModuleType',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='target', ctx=Store())],
                                            value=Call(
                                                func=Name(id='wrap_module', ctx=Load()),
                                                args=[
                                                    Name(id='target', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='attributes', ctx=Load()),
                                                        slice=Name(id='attrib', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='setattr', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='attrib', ctx=Load()),
                                            Name(id='target', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__repr__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_repr',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Import(
            names=[alias(name='dateutil', asname=None)],
        ),
        Assign(
            targets=[Name(id='mods', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='parser', kind=None),
                    Constant(value='relativedelta', kind=None),
                    Constant(value='rrule', kind=None),
                    Constant(value='tz', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        For(
            target=Name(id='mod', ctx=Store()),
            iter=Name(id='mods', ctx=Load()),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='__import__', ctx=Load()),
                        args=[
                            BinOp(
                                left=Constant(value='dateutil.%s', kind=None),
                                op=Mod(),
                                right=Name(id='mod', ctx=Load()),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            orelse=[],
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='datetime', ctx=Store())],
            value=Call(
                func=Name(id='wrap_module', ctx=Load()),
                args=[
                    Call(
                        func=Name(id='__import__', ctx=Load()),
                        args=[Constant(value='datetime', kind=None)],
                        keywords=[],
                    ),
                    List(
                        elts=[
                            Constant(value='date', kind=None),
                            Constant(value='datetime', kind=None),
                            Constant(value='time', kind=None),
                            Constant(value='timedelta', kind=None),
                            Constant(value='timezone', kind=None),
                            Constant(value='tzinfo', kind=None),
                            Constant(value='MAXYEAR', kind=None),
                            Constant(value='MINYEAR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='dateutil', ctx=Store())],
            value=Call(
                func=Name(id='wrap_module', ctx=Load()),
                args=[
                    Name(id='dateutil', ctx=Load()),
                    DictComp(
                        key=Name(id='mod', ctx=Load()),
                        value=Attribute(
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='dateutil', ctx=Load()),
                                    Name(id='mod', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            attr='__all__',
                            ctx=Load(),
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='mod', ctx=Store()),
                                iter=Name(id='mods', ctx=Load()),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='json', ctx=Store())],
            value=Call(
                func=Name(id='wrap_module', ctx=Load()),
                args=[
                    Call(
                        func=Name(id='__import__', ctx=Load()),
                        args=[Constant(value='json', kind=None)],
                        keywords=[],
                    ),
                    List(
                        elts=[
                            Constant(value='loads', kind=None),
                            Constant(value='dumps', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='time', ctx=Store())],
            value=Call(
                func=Name(id='wrap_module', ctx=Load()),
                args=[
                    Call(
                        func=Name(id='__import__', ctx=Load()),
                        args=[Constant(value='time', kind=None)],
                        keywords=[],
                    ),
                    List(
                        elts=[
                            Constant(value='time', kind=None),
                            Constant(value='strptime', kind=None),
                            Constant(value='strftime', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='pytz', ctx=Store())],
            value=Call(
                func=Name(id='wrap_module', ctx=Load()),
                args=[
                    Call(
                        func=Name(id='__import__', ctx=Load()),
                        args=[Constant(value='pytz', kind=None)],
                        keywords=[],
                    ),
                    List(
                        elts=[
                            Constant(value='utc', kind=None),
                            Constant(value='UTC', kind=None),
                            Constant(value='timezone', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
