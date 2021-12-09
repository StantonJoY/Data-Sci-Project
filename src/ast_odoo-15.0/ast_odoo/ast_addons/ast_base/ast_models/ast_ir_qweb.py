Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='textwrap',
            names=[alias(name='dedent', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='copy', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='markupsafe', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[
                alias(name='html', asname=None),
                alias(name='etree', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.safe_eval',
            names=[
                alias(name='check_values', asname=None),
                alias(name='assert_valid_codeobj', asname=None),
                alias(name='_BUILTINS', asname=None),
                alias(name='to_opcodes', asname=None),
                alias(name='_EXPR_OPCODES', asname=None),
                alias(name='_BLACKLIST', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='get_lang', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_resource_path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.profiler',
            names=[alias(name='QwebTracker', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.qweb',
            names=[alias(name='QWeb', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.assetsbundle',
            names=[alias(name='AssetsBundle', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_asset',
            names=[
                alias(name='can_aggregate', asname=None),
                alias(name='STYLE_EXTENSIONS', asname=None),
                alias(name='SCRIPT_EXTENSIONS', asname=None),
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
        Assign(
            targets=[Name(id='_SAFE_QWEB_OPCODES', ctx=Store())],
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
                                        Constant(value='LOAD_NAME', kind=None),
                                        Constant(value='LOAD_ATTR', kind=None),
                                        Constant(value='LOAD_FAST', kind=None),
                                        Constant(value='STORE_FAST', kind=None),
                                        Constant(value='UNPACK_SEQUENCE', kind=None),
                                        Constant(value='STORE_SUBSCR', kind=None),
                                        Constant(value='LOAD_GLOBAL', kind=None),
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
        ClassDef(
            name='IrQWeb',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
                Name(id='QWeb', ctx=Load()),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Base QWeb rendering engine\n    * to customize ``t-field`` rendering, subclass ``ir.qweb.field`` and\n      create new models called :samp:`ir.qweb.field.{widget}`\n    Beware that if you need extensions or alterations which could be\n    incompatible with other subsystems, you should create a local object\n    inheriting from ``ir.qweb`` and customize that.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_available_objects', ctx=Store())],
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[Name(id='_BUILTINS', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_empty_lines', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='\\n\\s*\\n', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_render',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='options', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' render(template, values, **options)\n\n        Render the template specified by the given name.\n\n        :param template: etree, xml_id, template name (see _get_template)\n            * Call the method ``load`` is not an etree.\n        :param dict values: template values to be used for rendering\n        :param options: used to compile the template (the dict available for the rendering is frozen)\n            * ``load`` (function) overrides the load method\n\n        :returns: bytes marked as markup-safe (decode to :class:`markupsafe.Markup`\n                  instead of `str`)\n        :rtype: MarkupSafe\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='compile_options', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dev_mode',
                                        value=Compare(
                                            left=Constant(value='qweb', kind=None),
                                            ops=[In()],
                                            comparators=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='tools', ctx=Load()),
                                                        attr='config',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='dev_mode', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='compile_options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='options', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[Name(id='template', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='values',
                                        value=Name(id='values', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='compile_options', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='values', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='__keep_empty_lines', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='markupsafe', ctx=Load()),
                                            attr='Markup',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='IrQWeb', ctx=Load()),
                                                        attr='_empty_lines',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='\n', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='result', ctx=Load()),
                                                            attr='strip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
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
                        If(
                            test=Compare(
                                left=Constant(value='data-pagebreak=', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='result', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Name(id='result', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='fragments', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='fragments_fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='result', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='fragment', ctx=Store()),
                            iter=Name(id='fragments', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='row', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='fragment', ctx=Load()),
                                            attr='iterfind',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.//tr[@data-pagebreak]', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='table', ctx=Store())],
                                            value=Call(
                                                func=Name(id='next', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='row', ctx=Load()),
                                                            attr='iterancestors',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='table', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='newtable', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='html', ctx=Load()),
                                                    attr='Element',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='table', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='attrib',
                                                        value=Call(
                                                            func=Name(id='dict', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='table', ctx=Load()),
                                                                    attr='attrib',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='thead', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='table', ctx=Load()),
                                                    attr='find',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='thead', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='thead', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='newtable', ctx=Load()),
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
                                                                args=[Name(id='thead', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='pos', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='row', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='data-pagebreak', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assert(
                                            test=Compare(
                                                left=Name(id='pos', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='before', kind=None),
                                                            Constant(value='after', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            msg=None,
                                        ),
                                        For(
                                            target=Name(id='sibling', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='row', ctx=Load()),
                                                            attr='getparent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='iterchildren',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='tr', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='sibling', ctx=Load()),
                                                        ops=[Is()],
                                                        comparators=[Name(id='row', ctx=Load())],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='pos', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='after', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='newtable', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='sibling', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Break(),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='newtable', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='sibling', ctx=Load())],
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
                                                    value=Name(id='table', ctx=Load()),
                                                    attr='addprevious',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='newtable', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='table', ctx=Load()),
                                                    attr='addprevious',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='html', ctx=Load()),
                                                            attr='Element',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='div', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='attrib',
                                                                value=Dict(
                                                                    keys=[Constant(value='style', kind=None)],
                                                                    values=[Constant(value='page-break-after: always', kind=None)],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='markupsafe', ctx=Load()),
                                    attr='Markup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='html', ctx=Load()),
                                                                attr='tostring',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='f', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='f', ctx=Store()),
                                                        iter=Name(id='fragments', ctx=Load()),
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
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='QwebTracker', ctx=Load()),
                            attr='wrap_render',
                            ctx=Load(),
                        ),
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_template_cache_keys',
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
                        Expr(
                            value=Constant(value=' Return the list of context keys to use for caching ``_get_template``. ', kind=None),
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='lang', kind=None),
                                    Constant(value='inherit_branding', kind=None),
                                    Constant(value='editable', kind=None),
                                    Constant(value='translatable', kind=None),
                                    Constant(value='edit_translations', kind=None),
                                    Constant(value='website_id', kind=None),
                                    Constant(value='profile', kind=None),
                                    Constant(value='raise_on_code', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='id_or_xml_id', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='id_or_xml_id', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='id_or_xml_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='id_or_xml_id', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='options',
                                        value=Name(id='options', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='conditional',
                                ctx=Load(),
                            ),
                            args=[
                                Compare(
                                    left=Constant(value='xml', kind=None),
                                    ops=[NotIn()],
                                    comparators=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='dev_mode', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                Call(
                                    func=Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='ormcache',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='id_or_xml_id', kind=None),
                                        Constant(value='tuple(options.get(k) for k in self._get_template_cache_keys())', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        Attribute(
                            value=Name(id='QwebTracker', ctx=Load()),
                            attr='wrap_compile',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_load',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='lang', kind=None),
                                    Attribute(
                                        value=Call(
                                            func=Name(id='get_lang', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='env',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='lang', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='env', ctx=Load()),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='lang', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Name(id='env', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='context',
                                                value=Call(
                                                    func=Name(id='dict', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='env', ctx=Load()),
                                                            attr='context',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Name(id='lang', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='view_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_view_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_read_template',
                                    ctx=Load(),
                                ),
                                args=[Name(id='view_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='is_child_view',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='view_name', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='view_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_view_id',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='view_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='view', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.ui.view', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='view_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Compare(
                                        left=Attribute(
                                            value=Name(id='view', ctx=Load()),
                                            attr='inherit_id',
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='int', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='is_child_view', ctx=Load()),
                                        args=[Name(id='name', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='view', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='node', ctx=Store()),
                                    iter=Name(id='view', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='t-name', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='t-name', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='name', ctx=Load())],
                                                                keywords=[],
                                                            ),
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
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='view', ctx=Load()),
                                            Name(id='view_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='template', ctx=Load()),
                                            Name(id='view_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_directives_eval_order',
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
                        Assign(
                            targets=[Name(id='directives', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_directives_eval_order',
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
                                    value=Name(id='directives', ctx=Load()),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='directives', ctx=Load()),
                                            attr='index',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='foreach', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='groups', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='directives', ctx=Load()),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='directives', ctx=Load()),
                                            attr='index',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='call', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='lang', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='directives', ctx=Load()),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='directives', ctx=Load()),
                                            attr='index',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='field', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='call-assets', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='directives', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_node',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='groups', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='t-groups', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='groups', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compile_node',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='directive', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compile_directive',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='directive', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='QwebTracker', ctx=Load()),
                            attr='wrap_compile_directive',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_groups',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compile `t-groups` expressions into a python code as a list of\n        strings.\n\n        The code will contain the condition `if self.user_has_groups(groups)`\n        part that wrap the rest of the compiled code of this element.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t-groups', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_flushText',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='if self.user_has_groups(', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[Name(id='groups', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='):', kind=None),
                                                ],
                                            ),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_compile_directives',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='el', ctx=Load()),
                                                        Name(id='options', ctx=Load()),
                                                        BinOp(
                                                            left=Name(id='indent', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_flushText',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='options', ctx=Load()),
                                                        BinOp(
                                                            left=Name(id='indent', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='pass', kind=None),
                                                            BinOp(
                                                                left=Name(id='indent', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='t-options-lang', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t-lang', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_node',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_call_assets',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" This special 't-call' tag can be used in order to aggregate/minify javascript and css assets", kind=None),
                        ),
                        If(
                            test=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='el', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='SyntaxError', ctx=Load()),
                                        args=[Constant(value='t-call-assets cannot contain children nodes', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_flushText',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Name(id='dedent', ctx=Load()),
                                                            args=[Constant(value='\n            t_call_assets_nodes = self._get_asset_nodes(%(xmlid)s, css=%(css)s, js=%(js)s, debug=values.get("debug"), async_load=%(async_load)s, defer_load=%(defer_load)s, lazy_load=%(lazy_load)s, media=%(media)s)\n            for index, (tagName, attrs, content) in enumerate(t_call_assets_nodes):\n                if index:\n                    yield \'\\n        \'\n                yield \'<\'\n                yield tagName\n            ', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='strip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Dict(
                                                    keys=[
                                                        Constant(value='xmlid', kind=None),
                                                        Constant(value='css', kind=None),
                                                        Constant(value='js', kind=None),
                                                        Constant(value='async_load', kind=None),
                                                        Constant(value='defer_load', kind=None),
                                                        Constant(value='lazy_load', kind=None),
                                                        Constant(value='media', kind=None),
                                                    ],
                                                    values=[
                                                        Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='el', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='t-call-assets', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_compile_bool',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='el', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='t-css', kind=None),
                                                                        Constant(value=True, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_compile_bool',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='el', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='t-js', kind=None),
                                                                        Constant(value=True, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_compile_bool',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='el', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='async_load', kind=None),
                                                                        Constant(value=False, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_compile_bool',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='el', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='defer_load', kind=None),
                                                                        Constant(value=False, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_compile_bool',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='el', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='lazy_load', kind=None),
                                                                        Constant(value=False, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        IfExp(
                                                            test=Call(
                                                                func=Attribute(
                                                                    value=Name(id='el', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='media', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            body=Call(
                                                                func=Name(id='repr', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='el', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='media', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            orelse=Constant(value=False, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_attributes',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='options', ctx=Load()),
                                            BinOp(
                                                left=Name(id='indent', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='dedent', ctx=Load()),
                                                        args=[Constant(value="\n                if not content and tagName in self._void_elements:\n                    yield '/>'\n                else:\n                    yield '>'\n                    if content:\n                      yield content\n                    yield '</'\n                    yield tagName\n                    yield '>'\n                ", kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                left=Name(id='indent', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_asset_bundle',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle_name', annotation=None, type_comment=None),
                            arg(arg='files', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='css', annotation=None, type_comment=None),
                            arg(arg='js', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='AssetsBundle', ctx=Load()),
                                args=[
                                    Name(id='bundle_name', ctx=Load()),
                                    Name(id='files', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='env',
                                        value=Name(id='env', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='css',
                                        value=Name(id='css', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='js',
                                        value=Name(id='js', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_asset_nodes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='css', annotation=None, type_comment=None),
                            arg(arg='js', annotation=None, type_comment=None),
                            arg(arg='debug', annotation=None, type_comment=None),
                            arg(arg='async_load', annotation=None, type_comment=None),
                            arg(arg='defer_load', annotation=None, type_comment=None),
                            arg(arg='lazy_load', annotation=None, type_comment=None),
                            arg(arg='media', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Generates asset nodes.\n        If debug=assets, the assets will be regenerated when a file which composes them has been modified.\n        Else, the assets will be generated only once and then stored in cache.\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='debug', ctx=Load()),
                                    Compare(
                                        left=Constant(value='assets', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='debug', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_generate_asset_nodes',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='bundle', ctx=Load()),
                                            Name(id='css', ctx=Load()),
                                            Name(id='js', ctx=Load()),
                                            Name(id='debug', ctx=Load()),
                                            Name(id='async_load', ctx=Load()),
                                            Name(id='defer_load', ctx=Load()),
                                            Name(id='lazy_load', ctx=Load()),
                                            Name(id='media', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_generate_asset_nodes_cache',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='bundle', ctx=Load()),
                                            Name(id='css', ctx=Load()),
                                            Name(id='js', ctx=Load()),
                                            Name(id='debug', ctx=Load()),
                                            Name(id='async_load', ctx=Load()),
                                            Name(id='defer_load', ctx=Load()),
                                            Name(id='lazy_load', ctx=Load()),
                                            Name(id='media', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_generate_asset_nodes_cache',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='css', annotation=None, type_comment=None),
                            arg(arg='js', annotation=None, type_comment=None),
                            arg(arg='debug', annotation=None, type_comment=None),
                            arg(arg='async_load', annotation=None, type_comment=None),
                            arg(arg='defer_load', annotation=None, type_comment=None),
                            arg(arg='lazy_load', annotation=None, type_comment=None),
                            arg(arg='media', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_generate_asset_nodes',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bundle', ctx=Load()),
                                    Name(id='css', ctx=Load()),
                                    Name(id='js', ctx=Load()),
                                    Name(id='debug', ctx=Load()),
                                    Name(id='async_load', ctx=Load()),
                                    Name(id='defer_load', ctx=Load()),
                                    Name(id='lazy_load', ctx=Load()),
                                    Name(id='media', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='conditional',
                                ctx=Load(),
                            ),
                            args=[
                                Compare(
                                    left=Constant(value='xml', kind=None),
                                    ops=[NotIn()],
                                    comparators=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='dev_mode', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                Call(
                                    func=Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='ormcache_context',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='bundle', kind=None),
                                        Constant(value='css', kind=None),
                                        Constant(value='js', kind=None),
                                        Constant(value='debug', kind=None),
                                        Constant(value='async_load', kind=None),
                                        Constant(value='defer_load', kind=None),
                                        Constant(value='lazy_load', kind=None),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='keys',
                                            value=Tuple(
                                                elts=[
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='lang', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_generate_asset_nodes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='css', annotation=None, type_comment=None),
                            arg(arg='js', annotation=None, type_comment=None),
                            arg(arg='debug', annotation=None, type_comment=None),
                            arg(arg='async_load', annotation=None, type_comment=None),
                            arg(arg='defer_load', annotation=None, type_comment=None),
                            arg(arg='lazy_load', annotation=None, type_comment=None),
                            arg(arg='media', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='nodeAttrs', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='css', ctx=Load()),
                                    Name(id='media', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='nodeAttrs', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='media', kind=None)],
                                        values=[Name(id='media', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='files', ctx=Store()),
                                        Name(id='remains', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_asset_content',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bundle', ctx=Load()),
                                    Name(id='nodeAttrs', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='defer_load',
                                        value=Name(id='defer_load', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lazy_load',
                                        value=Name(id='lazy_load', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='asset', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_asset_bundle',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bundle', ctx=Load()),
                                    Name(id='files', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='env',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='css',
                                        value=Name(id='css', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='js',
                                        value=Name(id='js', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remains', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='node', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='node', ctx=Store()),
                                        iter=Name(id='remains', ctx=Load()),
                                        ifs=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='css', ctx=Load()),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='link', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='js', ctx=Load()),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='script', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='remains', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='asset', ctx=Load()),
                                        attr='to_node',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='css',
                                            value=Name(id='css', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='js',
                                            value=Name(id='js', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='debug',
                                            value=Name(id='debug', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='async_load',
                                            value=Name(id='async_load', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='defer_load',
                                            value=Name(id='defer_load', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='lazy_load',
                                            value=Name(id='lazy_load', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_asset_link_urls',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='asset_nodes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_asset_nodes',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bundle', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='js',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=ListComp(
                                elt=Subscript(
                                    value=Subscript(
                                        value=Name(id='node', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='href', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='node', ctx=Store()),
                                        iter=Name(id='asset_nodes', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='node', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='link', kind=None)],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_asset_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='nodeAttrs', annotation=None, type_comment=None),
                            arg(arg='defer_load', annotation=None, type_comment=None),
                            arg(arg='lazy_load', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='asset_paths', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.asset', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_asset_paths',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bundle',
                                        value=Name(id='bundle', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='css',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='js',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='files', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remains', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='path', ctx=Store()),
                                    Starred(
                                        value=Name(id='_', ctx=Store()),
                                        ctx=Store(),
                                    ),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='asset_paths', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='ext', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='path', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='.', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='is_js', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='ext', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='SCRIPT_EXTENSIONS', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='is_css', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='ext', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='STYLE_EXTENSIONS', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='is_js', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='is_css', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='mimetype', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='is_js', ctx=Load()),
                                        body=Constant(value='text/javascript', kind=None),
                                        orelse=BinOp(
                                            left=Constant(value='text/%s', kind=None),
                                            op=Mod(),
                                            right=Name(id='ext', ctx=Load()),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='can_aggregate', ctx=Load()),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='segments', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='segment', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='segment', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='path', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='/', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[Name(id='segment', ctx=Load())],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='files', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='atype', kind=None),
                                                            Constant(value='url', kind=None),
                                                            Constant(value='filename', kind=None),
                                                            Constant(value='content', kind=None),
                                                            Constant(value='media', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='mimetype', ctx=Load()),
                                                            Name(id='path', ctx=Load()),
                                                            IfExp(
                                                                test=Name(id='segments', ctx=Load()),
                                                                body=Call(
                                                                    func=Name(id='get_resource_path', ctx=Load()),
                                                                    args=[
                                                                        Starred(
                                                                            value=Name(id='segments', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                orelse=Constant(value=None, kind=None),
                                                            ),
                                                            Constant(value='', kind=None),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='nodeAttrs', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='nodeAttrs', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='media', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Name(id='is_js', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='tag', ctx=Store())],
                                                    value=Constant(value='script', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='attributes', ctx=Store())],
                                                    value=Dict(
                                                        keys=[Constant(value='type', kind=None)],
                                                        values=[Name(id='mimetype', ctx=Load())],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='attributes', ctx=Load()),
                                                            slice=IfExp(
                                                                test=Name(id='lazy_load', ctx=Load()),
                                                                body=Constant(value='data-src', kind=None),
                                                                orelse=Constant(value='src', kind=None),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='path', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='defer_load', ctx=Load()),
                                                            Name(id='lazy_load', ctx=Load()),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='attributes', ctx=Load()),
                                                                    slice=Constant(value='defer', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='defer', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='tag', ctx=Store())],
                                                    value=Constant(value='link', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='attributes', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='rel', kind=None),
                                                            Constant(value='href', kind=None),
                                                            Constant(value='media', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='mimetype', ctx=Load()),
                                                            Constant(value='stylesheet', kind=None),
                                                            Name(id='path', ctx=Load()),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='nodeAttrs', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='nodeAttrs', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='media', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='remains', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='tag', ctx=Load()),
                                                            Name(id='attributes', ctx=Load()),
                                                            Constant(value='', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='files', ctx=Load()),
                                    Name(id='remains', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache_context',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='bundle', kind=None),
                                Constant(value='nodeAttrs and nodeAttrs.get("media")', kind=None),
                                Constant(value='defer_load', kind=None),
                                Constant(value='lazy_load', kind=None),
                            ],
                            keywords=[
                                keyword(
                                    arg='keys',
                                    value=Tuple(
                                        elts=[
                                            Constant(value='website_id', kind=None),
                                            Constant(value='lang', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_field',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='expression', annotation=None, type_comment=None),
                            arg(arg='tagName', annotation=None, type_comment=None),
                            arg(arg='field_options', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Name(id='field_name', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='template_options', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='options', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='tagName', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='tagName', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='expression', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='expression', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='field_options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='widget', kind=None),
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='type',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='inherit_branding', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='inherit_branding', kind=None),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='inherit_branding_auto', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='check_access_rights',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='write', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='inherit_branding', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='inherit_branding', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='translate', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='edit_translations', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='translatable', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='translate',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='translate', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='translate', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='ir.qweb.field.', kind=None),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='converter', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='model', ctx=Load()),
                                    ops=[In()],
                                    comparators=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='model', ctx=Load()),
                                    ctx=Load(),
                                ),
                                orelse=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='ir.qweb.field', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='converter', ctx=Load()),
                                    attr='record_to_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                    Name(id='field_options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attributes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='converter', ctx=Load()),
                                    attr='attributes',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                    Name(id='field_options', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='attributes', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='inherit_branding', ctx=Load()),
                                            Name(id='translate', ctx=Load()),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_widget',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='expression', annotation=None, type_comment=None),
                            arg(arg='tagName', annotation=None, type_comment=None),
                            arg(arg='field_options', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='template_options', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='options', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='field_options', ctx=Load()),
                                slice=Constant(value='widget', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='tagName', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='tagName', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='expression', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='expression', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='ir.qweb.field.', kind=None),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='field_options', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='converter', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='model', ctx=Load()),
                                    ops=[In()],
                                    comparators=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='model', ctx=Load()),
                                    ctx=Load(),
                                ),
                                orelse=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='ir.qweb.field', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='converter', ctx=Load()),
                                    attr='value_to_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='field_options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attributes', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='attributes', ctx=Load()),
                                    slice=Constant(value='data-oe-type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='field_options', ctx=Load()),
                                slice=Constant(value='type', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='attributes', ctx=Load()),
                                    slice=Constant(value='data-oe-expression', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='field_options', ctx=Load()),
                                slice=Constant(value='expression', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='attributes', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                    Constant(value=None, kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prepare the context that will be sent to the evaluated function.\n\n        :param values: template values to be used for rendering\n        :param options: frozen dict of compilation parameters.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check_values', ctx=Load()),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='true', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='false', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='request', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='request', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='request', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_prepare_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='values', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_expr',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='expr', annotation=None, type_comment=None),
                            arg(arg='raise_on_missing', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Compiles a purported Python expression to compiled code, verifies\n        that it's safe (according to safe_eval's semantics) and alter its\n        variable references to access values data instead\n\n        :param expr: string\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='namespace_expr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compile_expr',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expr', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='raise_on_missing',
                                        value=Name(id='raise_on_missing', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_valid_codeobj', ctx=Load()),
                                args=[
                                    Name(id='_SAFE_QWEB_OPCODES', ctx=Load()),
                                    Call(
                                        func=Name(id='compile', ctx=Load()),
                                        args=[
                                            Name(id='namespace_expr', ctx=Load()),
                                            Constant(value='<>', kind=None),
                                            Constant(value='eval', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expr', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='namespace_expr', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
