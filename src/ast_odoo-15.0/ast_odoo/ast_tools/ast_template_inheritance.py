Module(
    body=[
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml.builder',
            names=[alias(name='E', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='copy', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='SKIPPED_ELEMENT_TYPES', asname=None),
                alias(name='html_escape', asname=None),
            ],
            level=0,
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
            name='add_text_before',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='node', annotation=None, type_comment=None),
                    arg(arg='text', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Add text before ``node`` in its XML tree. ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='text', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='prev', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='node', ctx=Load()),
                            attr='getprevious',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='prev', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='prev', ctx=Load()),
                                    attr='tail',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=BoolOp(
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            value=Name(id='prev', ctx=Load()),
                                            attr='tail',
                                            ctx=Load(),
                                        ),
                                        Constant(value='', kind=None),
                                    ],
                                ),
                                op=Add(),
                                right=Name(id='text', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='parent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='getparent',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='parent', ctx=Load()),
                                    attr='text',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=BoolOp(
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            value=Name(id='parent', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        Constant(value='', kind=None),
                                    ],
                                ),
                                op=Add(),
                                right=Name(id='text', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='add_text_inside',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='node', annotation=None, type_comment=None),
                    arg(arg='text', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Add text inside ``node``. ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='text', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='len', ctx=Load()),
                        args=[Name(id='node', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='node', ctx=Load()),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='tail',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=BoolOp(
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            value=Subscript(
                                                value=Name(id='node', ctx=Load()),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='tail',
                                            ctx=Load(),
                                        ),
                                        Constant(value='', kind=None),
                                    ],
                                ),
                                op=Add(),
                                right=Name(id='text', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='text',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=BoolOp(
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        Constant(value='', kind=None),
                                    ],
                                ),
                                op=Add(),
                                right=Name(id='text', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='remove_element',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='node', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Remove ``node`` but not its tail, from its XML tree. ', kind=None),
                ),
                Expr(
                    value=Call(
                        func=Name(id='add_text_before', ctx=Load()),
                        args=[
                            Name(id='node', ctx=Load()),
                            Attribute(
                                value=Name(id='node', ctx=Load()),
                                attr='tail',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='node', ctx=Load()),
                            attr='tail',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='getparent',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='remove',
                            ctx=Load(),
                        ),
                        args=[Name(id='node', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='locate_node',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='arch', annotation=None, type_comment=None),
                    arg(arg='spec', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Locate a node in a source (parent) architecture.\n\n    Given a complete source (parent) architecture (i.e. the field\n    `arch` in a view), and a 'spec' node (a node in an inheriting\n    view that specifies the location in the source view of what\n    should be changed), return (if it exists) the node in the\n    source view matching the specification.\n\n    :param arch: a parent architecture to modify\n    :param spec: a modifying node in an inheriting view\n    :return: a node in the source matching the spec\n    ", kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='spec', ctx=Load()),
                            attr='tag',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='xpath', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='expr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='spec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='expr', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='xPath', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='ETXPath',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='expr', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='etree', ctx=Load()),
                                        attr='XPathSyntaxError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='XPathSyntaxError while parsing xpath %r', kind=None),
                                                    Name(id='expr', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(exc=None, cause=None),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='nodes', ctx=Store())],
                            value=Call(
                                func=Name(id='xPath', ctx=Load()),
                                args=[Name(id='arch', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id='nodes', ctx=Load()),
                                body=Subscript(
                                    value=Name(id='nodes', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Constant(value=None, kind=None),
                            ),
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='spec', ctx=Load()),
                                    attr='tag',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='field', kind=None)],
                            ),
                            body=[
                                For(
                                    target=Name(id='node', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='arch', ctx=Load()),
                                            attr='iter',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='field', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='name', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='spec', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Name(id='node', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
                For(
                    target=Name(id='node', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='arch', ctx=Load()),
                            attr='iter',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='spec', ctx=Load()),
                                attr='tag',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='node', ctx=Load()),
                                    Name(id='SKIPPED_ELEMENT_TYPES', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='all', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Call(
                                                func=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='attr', ctx=Load())],
                                                keywords=[],
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='spec', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='attr', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='attr', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='spec', ctx=Load()),
                                                    attr='attrib',
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='attr', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='position', kind=None),
                                                                    Constant(value='version', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='spec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='version', kind=None)],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='spec', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='version', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='arch', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='version', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=None, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='node', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Constant(value=None, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='apply_inheritance_specs',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='source', annotation=None, type_comment=None),
                    arg(arg='specs_tree', annotation=None, type_comment=None),
                    arg(arg='inherit_branding', annotation=None, type_comment=None),
                    arg(arg='pre_locate', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='s', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Constant(value=True, kind=None),
                    ),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Apply an inheriting view (a descendant of the base view)\n\n    Apply to a source architecture all the spec nodes (i.e. nodes\n    describing where and what changes to apply to some parent\n    architecture) given by an inheriting view.\n\n    :param Element source: a parent architecture to modify\n    :param Element specs_tree: a modifying architecture in an inheriting view\n    :param bool inherit_branding:\n    :param pre_locate: function that is executed before locating a node.\n                        This function receives an arch as argument.\n                        This is required by studio to properly handle group_ids.\n    :return: a modified source where the specs are applied\n    :rtype: Element\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='specs', ctx=Store())],
                    value=IfExp(
                        test=Call(
                            func=Name(id='isinstance', ctx=Load()),
                            args=[
                                Name(id='specs_tree', ctx=Load()),
                                Name(id='list', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                        body=Name(id='specs_tree', ctx=Load()),
                        orelse=List(
                            elts=[Name(id='specs_tree', ctx=Load())],
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='extract',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='spec', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Utility function that locates a node given a specification, remove\n        it from the source and returns it.\n        ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='spec', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Invalid specification for moved nodes: %r', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='etree', ctx=Load()),
                                                            attr='tostring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='spec', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='encoding',
                                                                value=Constant(value='unicode', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='pre_locate', ctx=Load()),
                                args=[Name(id='spec', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='to_extract', ctx=Store())],
                            value=Call(
                                func=Name(id='locate_node', ctx=Load()),
                                args=[
                                    Name(id='source', ctx=Load()),
                                    Name(id='spec', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='to_extract', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='remove_element', ctx=Load()),
                                        args=[Name(id='to_extract', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='to_extract', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Element %r cannot be located in parent view', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='etree', ctx=Load()),
                                                            attr='tostring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='spec', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='encoding',
                                                                value=Constant(value='unicode', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                While(
                    test=Call(
                        func=Name(id='len', ctx=Load()),
                        args=[Name(id='specs', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='spec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='specs', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='spec', ctx=Load()),
                                    Name(id='SKIPPED_ELEMENT_TYPES', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='spec', ctx=Load()),
                                    attr='tag',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='data', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='specs', ctx=Store()),
                                    op=Add(),
                                    value=ListComp(
                                        elt=Name(id='c', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='c', ctx=Store()),
                                                iter=Name(id='spec', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                                Continue(),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='pre_locate', ctx=Load()),
                                args=[Name(id='spec', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='node', ctx=Store())],
                            value=Call(
                                func=Name(id='locate_node', ctx=Load()),
                                args=[
                                    Name(id='source', ctx=Load()),
                                    Name(id='spec', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='node', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pos', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='spec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='position', kind=None),
                                            Constant(value='inside', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='pos', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='replace', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='mode', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='spec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='mode', kind=None),
                                                    Constant(value='outer', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='mode', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='outer', kind=None)],
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='loc', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='spec', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=".//*[text()='$0']", kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='loc', ctx=Load()),
                                                                    attr='text',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='loc', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='copy', ctx=Load()),
                                                                            attr='deepcopy',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='node', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='node', ctx=Load()),
                                                                attr='getparent',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[Is()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='spec_content', ctx=Store())],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='comment', ctx=Store())],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        For(
                                                            target=Name(id='content', ctx=Store()),
                                                            iter=Name(id='spec', ctx=Load()),
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='content', ctx=Load()),
                                                                            attr='tag',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[IsNot()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='etree', ctx=Load()),
                                                                                attr='Comment',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='spec_content', ctx=Store())],
                                                                            value=Name(id='content', ctx=Load()),
                                                                            type_comment=None,
                                                                        ),
                                                                        Break(),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[Name(id='comment', ctx=Store())],
                                                                            value=Name(id='content', ctx=Load()),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='source', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='copy', ctx=Load()),
                                                                    attr='deepcopy',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='spec_content', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='t_name', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='t-name', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='t_name', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='source', ctx=Load()),
                                                                            attr='set',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='t-name', kind=None),
                                                                            Name(id='t_name', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='comment', ctx=Load()),
                                                                ops=[IsNot()],
                                                                comparators=[Constant(value=None, kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='text', ctx=Store())],
                                                                    value=Attribute(
                                                                        value=Name(id='source', ctx=Load()),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='source', ctx=Load()),
                                                                            attr='text',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value=None, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='comment', ctx=Load()),
                                                                            attr='tail',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='text', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='source', ctx=Load()),
                                                                            attr='insert',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value=0, kind=None),
                                                                            Name(id='comment', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='replaced_node_tag', ctx=Store())],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        For(
                                                            target=Name(id='child', ctx=Store()),
                                                            iter=Name(id='spec', ctx=Load()),
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='child', ctx=Load()),
                                                                                attr='get',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='position', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='move', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='child', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='extract', ctx=Load()),
                                                                                args=[Name(id='child', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='inherit_branding', ctx=Load()),
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=Name(id='replaced_node_tag', ctx=Load()),
                                                                            ),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='child', ctx=Load()),
                                                                                    attr='tag',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[IsNot()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='etree', ctx=Load()),
                                                                                        attr='Comment',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='child', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Constant(value='meta-oe-xpath-replacing', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='node', ctx=Load()),
                                                                                        attr='tag',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='replaced_node_tag', ctx=Store())],
                                                                            value=Attribute(
                                                                                value=Name(id='node', ctx=Load()),
                                                                                attr='tag',
                                                                                ctx=Load(),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='node', ctx=Load()),
                                                                            attr='addprevious',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='child', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='node', ctx=Load()),
                                                                            attr='getparent',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='remove',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='node', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='mode', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='inner', kind=None)],
                                                    ),
                                                    body=[
                                                        For(
                                                            target=Name(id='child', ctx=Store()),
                                                            iter=Name(id='node', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='node', ctx=Load()),
                                                                            attr='remove',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='child', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='text',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        For(
                                                            target=Name(id='child', ctx=Store()),
                                                            iter=Name(id='spec', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='node', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='copy', ctx=Load()),
                                                                                    attr='deepcopy',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='child', ctx=Load())],
                                                                                keywords=[],
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
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='text',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Attribute(
                                                                value=Name(id='spec', ctx=Load()),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValueError', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Invalid mode attribute:', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=BinOp(
                                                                            left=Constant(value=" '%s'", kind=None),
                                                                            op=Mod(),
                                                                            right=Name(id='mode', ctx=Load()),
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
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='pos', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='attributes', kind=None)],
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='child', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='spec', ctx=Load()),
                                                            attr='getiterator',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='attribute', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='attribute', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='child', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='name', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='value', ctx=Store())],
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='child', ctx=Load()),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='', kind=None),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='child', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='add', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='child', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='remove', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assert(
                                                                    test=UnaryOp(
                                                                        op=Not(),
                                                                        operand=Attribute(
                                                                            value=Name(id='child', ctx=Load()),
                                                                            attr='text',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    msg=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='separator', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='child', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='separator', kind=None),
                                                                            Constant(value=',', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='separator', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value=' ', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='separator', ctx=Store())],
                                                                            value=Constant(value=None, kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='to_add', ctx=Store())],
                                                                    value=GeneratorExp(
                                                                        elt=Name(id='s', ctx=Load()),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='s', ctx=Store()),
                                                                                iter=GeneratorExp(
                                                                                    elt=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='s', ctx=Load()),
                                                                                            attr='strip',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    generators=[
                                                                                        comprehension(
                                                                                            target=Name(id='s', ctx=Store()),
                                                                                            iter=Call(
                                                                                                func=Attribute(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='child', ctx=Load()),
                                                                                                            attr='get',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            Constant(value='add', kind=None),
                                                                                                            Constant(value='', kind=None),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    attr='split',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='separator', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            ifs=[],
                                                                                            is_async=0,
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                ifs=[Name(id='s', ctx=Load())],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='to_remove', ctx=Store())],
                                                                    value=SetComp(
                                                                        elt=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='s', ctx=Load()),
                                                                                attr='strip',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='s', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='child', ctx=Load()),
                                                                                                attr='get',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Constant(value='remove', kind=None),
                                                                                                Constant(value='', kind=None),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='split',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Name(id='separator', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                ifs=[],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='values', ctx=Store())],
                                                                    value=GeneratorExp(
                                                                        elt=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='s', ctx=Load()),
                                                                                attr='strip',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='s', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='node', ctx=Load()),
                                                                                                attr='get',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Name(id='attribute', ctx=Load()),
                                                                                                Constant(value='', kind=None),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='split',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Name(id='separator', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                ifs=[],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='value', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    Name(id='separator', ctx=Load()),
                                                                                    Constant(value=' ', kind=None),
                                                                                ],
                                                                            ),
                                                                            attr='join',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='itertools', ctx=Load()),
                                                                                    attr='chain',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    GeneratorExp(
                                                                                        elt=Name(id='v', ctx=Load()),
                                                                                        generators=[
                                                                                            comprehension(
                                                                                                target=Name(id='v', ctx=Store()),
                                                                                                iter=Name(id='values', ctx=Load()),
                                                                                                ifs=[
                                                                                                    Compare(
                                                                                                        left=Name(id='v', ctx=Load()),
                                                                                                        ops=[NotIn()],
                                                                                                        comparators=[Name(id='to_remove', ctx=Load())],
                                                                                                    ),
                                                                                                ],
                                                                                                is_async=0,
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    Name(id='to_add', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=Name(id='value', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='node', ctx=Load()),
                                                                            attr='set',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='attribute', ctx=Load()),
                                                                            Name(id='value', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='attribute', ctx=Load()),
                                                                        ops=[In()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='node', ctx=Load()),
                                                                                attr='attrib',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Delete(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='node', ctx=Load()),
                                                                                        attr='attrib',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Name(id='attribute', ctx=Load()),
                                                                                    ctx=Del(),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='pos', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='inside', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='add_text_inside', ctx=Load()),
                                                                args=[
                                                                    Name(id='node', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='spec', ctx=Load()),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        For(
                                                            target=Name(id='child', ctx=Store()),
                                                            iter=Name(id='spec', ctx=Load()),
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='child', ctx=Load()),
                                                                                attr='get',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='position', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='move', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='child', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='extract', ctx=Load()),
                                                                                args=[Name(id='child', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='node', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='child', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='pos', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='after', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='sentinel', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='E', ctx=Load()),
                                                                            attr='sentinel',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='node', ctx=Load()),
                                                                            attr='addnext',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='sentinel', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Name(id='add_text_before', ctx=Load()),
                                                                        args=[
                                                                            Name(id='sentinel', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='spec', ctx=Load()),
                                                                                attr='text',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                For(
                                                                    target=Name(id='child', ctx=Store()),
                                                                    iter=Name(id='spec', ctx=Load()),
                                                                    body=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='child', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='position', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='move', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='child', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Name(id='extract', ctx=Load()),
                                                                                        args=[Name(id='child', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='sentinel', ctx=Load()),
                                                                                    attr='addprevious',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='child', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Name(id='remove_element', ctx=Load()),
                                                                        args=[Name(id='sentinel', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='pos', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='before', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Name(id='add_text_before', ctx=Load()),
                                                                                args=[
                                                                                    Name(id='node', ctx=Load()),
                                                                                    Attribute(
                                                                                        value=Name(id='spec', ctx=Load()),
                                                                                        attr='text',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        For(
                                                                            target=Name(id='child', ctx=Store()),
                                                                            iter=Name(id='spec', ctx=Load()),
                                                                            body=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='child', ctx=Load()),
                                                                                                attr='get',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='position', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='move', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='child', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Name(id='extract', ctx=Load()),
                                                                                                args=[Name(id='child', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                ),
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='node', ctx=Load()),
                                                                                            attr='addprevious',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='child', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Raise(
                                                                            exc=Call(
                                                                                func=Name(id='ValueError', ctx=Load()),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Call(
                                                                                            func=Name(id='_', ctx=Load()),
                                                                                            args=[Constant(value="Invalid position attribute: '%s'", kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Mod(),
                                                                                        right=Name(id='pos', ctx=Load()),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            cause=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='attrs', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=BinOp(
                                                    left=Constant(value=' %s="%s"', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Name(id='attr', ctx=Load()),
                                                            Call(
                                                                func=Name(id='html_escape', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='spec', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='attr', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='attr', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='spec', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Name(id='attr', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='position', kind=None)],
                                                            ),
                                                        ],
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
                                    targets=[Name(id='tag', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='<%s%s>', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='spec', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                                Name(id='attrs', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value="Element '%s' cannot be located in parent view", kind=None),
                                                    Name(id='tag', ctx=Load()),
                                                ],
                                                keywords=[],
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
                ),
                Return(
                    value=Name(id='source', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
