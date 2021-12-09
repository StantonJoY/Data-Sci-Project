Module(
    body=[
        Expr(
            value=Constant(value='Utilities for generating, parsing and checking XML/XSD files on top of the lxml.etree module.', kind=None),
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='io',
            names=[alias(name='BytesIO', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='odoo_resolver',
            bases=[
                Attribute(
                    value=Name(id='etree', ctx=Load()),
                    attr='Resolver',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Odoo specific file resolver that can be added to the XML Parser.\n\n    It will search filenames in the ir.attachments\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='env', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='resolve',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='id', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Search url in ``ir.attachment`` and return the resolved content.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='url', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='attachment', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='resolve_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64decode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='datas',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='context', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='_check_with_xsd',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='tree_or_str', annotation=None, type_comment=None),
                    arg(arg='stream', annotation=None, type_comment=None),
                    arg(arg='env', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Check an XML against an XSD schema.\n\n    This will raise a UserError if the XML file is not valid according to the\n    XSD file.\n    :param tree_or_str (etree, str): representation of the tree to be checked\n    :param stream (io.IOBase, str): the byte stream used to build the XSD schema.\n        If env is given, it can also be the name of an attachment in the filestore\n    :param env (odoo.api.Environment): If it is given, it enables resolving the\n        imports of the schema in the filestore with ir.attachments.\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='isinstance', ctx=Load()),
                            args=[
                                Name(id='tree_or_str', ctx=Load()),
                                Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='_Element',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tree_or_str', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tree_or_str', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='parser', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='XMLParser',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='env', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='parser', ctx=Load()),
                                        attr='resolvers',
                                        ctx=Load(),
                                    ),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='odoo_resolver', ctx=Load()),
                                        args=[Name(id='env', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='stream', ctx=Load()),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='stream', ctx=Load()),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.xsd', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='ir.attachment', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='stream', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='attachment', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='FileNotFoundError', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='stream', ctx=Store())],
                                    value=Call(
                                        func=Name(id='BytesIO', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64decode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='datas',
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
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='xsd_schema', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='XMLSchema',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='parse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='stream', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='parser',
                                        value=Name(id='parser', ctx=Load()),
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xsd_schema', ctx=Load()),
                                    attr='assertValid',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tree_or_str', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Name(id='etree', ctx=Load()),
                                attr='DocumentInvalid',
                                ctx=Load(),
                            ),
                            name='xml_errors',
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='\n', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='e', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='e', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='xml_errors', ctx=Load()),
                                                                    attr='error_log',
                                                                    ctx=Load(),
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
            name='create_xml_node_chain',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='first_parent_node', annotation=None, type_comment=None),
                    arg(arg='nodes_list', annotation=None, type_comment=None),
                    arg(arg='last_node_value', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value="Generate a hierarchical chain of nodes.\n\n    Each new node being the child of the previous one based on the tags contained\n    in `nodes_list`, under the given node `first_parent_node`.\n    :param first_parent_node (etree._Element): parent of the created tree/chain\n    :param nodes_list (iterable<str>): tag names to be created\n    :param last_node_value (str): if specified, set the last node's text to this value\n    :returns (list<etree._Element>): the list of created nodes\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='res', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='current_node', ctx=Store())],
                    value=Name(id='first_parent_node', ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='tag', ctx=Store()),
                    iter=Name(id='nodes_list', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='current_node', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='SubElement',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='current_node', ctx=Load()),
                                    Name(id='tag', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='current_node', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='last_node_value', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='current_node', ctx=Load()),
                                    attr='text',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='last_node_value', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='res', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='create_xml_node',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='parent_node', annotation=None, type_comment=None),
                    arg(arg='node_name', annotation=None, type_comment=None),
                    arg(arg='node_value', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Create a new node.\n\n    :param parent_node (etree._Element): parent of the created node\n    :param node_name (str): name of the created node\n    :param node_value (str): value of the created node (optional)\n    :returns (etree._Element):\n    ', kind=None),
                ),
                Return(
                    value=Subscript(
                        value=Call(
                            func=Name(id='create_xml_node_chain', ctx=Load()),
                            args=[
                                Name(id='parent_node', ctx=Load()),
                                List(
                                    elts=[Name(id='node_name', ctx=Load())],
                                    ctx=Load(),
                                ),
                                Name(id='node_value', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
