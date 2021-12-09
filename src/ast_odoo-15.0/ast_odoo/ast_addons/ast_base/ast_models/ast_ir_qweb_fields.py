Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='io',
            names=[alias(name='BytesIO', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='babel', asname=None)],
        ),
        Import(
            names=[alias(name='babel.dates', asname=None)],
        ),
        ImportFrom(
            module='markupsafe',
            names=[
                alias(name='Markup', asname='M'),
                alias(name='escape', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='PIL',
            names=[alias(name='Image', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[
                alias(name='etree', asname=None),
                alias(name='html', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
                alias(name='_lt', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='posix_to_ldml', asname=None),
                alias(name='float_utils', asname=None),
                alias(name='format_date', asname=None),
                alias(name='format_duration', asname=None),
                alias(name='pycompat', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.mail',
            names=[alias(name='safe_attrs', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[
                alias(name='get_lang', asname=None),
                alias(name='babel_locale_parse', asname=None),
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
            name='nl2br',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='string', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Converts newlines to HTML linebreaks in ``string``. returns\n    the unicode result\n\n    :param str string:\n    :rtype: unicode\n    ', kind=None),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='to_text',
                                    ctx=Load(),
                                ),
                                args=[Name(id='string', ctx=Load())],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='\n', kind=None),
                            Call(
                                func=Name(id='M', ctx=Load()),
                                args=[Constant(value='<br>\n', kind=None)],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='FieldConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Used to convert a t-field specification into an output HTML field.\n\n    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:\n\n    * converts the record value to html using :meth:`~.record_to_html`\n    * generates the metadata attributes (``data-oe-``) to set on the root\n      result node\n    * generates the root result node itself through :meth:`~.render_element`\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            value=Constant(value="\n            Get the available option informations.\n\n            Returns a dict of dict with:\n            * key equal to the option key.\n            * dict: type, params, name, description, default_value\n            * type:\n                'string'\n                'integer'\n                'float'\n                'model' (e.g. 'res.partner')\n                'array'\n                'selection' (e.g. [key1, key2...])\n        ", kind=None),
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
                        ),
                    ],
                    decorator_list=[
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
                    name='attributes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" attributes(record, field_name, field, options, values)\n\n        Generates the metadata attributes (prefixed by ``data-oe-``) for the\n        root node of the field conversion.\n\n        The default attributes are:\n\n        * ``model``, the name of the record's model\n        * ``id`` the id of the record to which the field belongs\n        * ``type`` the logical field type (widget, may not match the field's\n          ``type``, may not be any Field subclass name)\n        * ``translate``, a boolean flag (``0`` or ``1``) denoting whether the\n          field is translatable\n        * ``readonly``, has this attribute if the field is readonly\n        * ``expression``, the original expression\n\n        :returns: dict (attribute name, attribute value).\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='inherit_branding', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='translate', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='data', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='data-oe-model', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='record', ctx=Load()),
                                attr='_name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='data-oe-id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='record', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='data-oe-field', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='field', ctx=Load()),
                                attr='name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='data-oe-type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='data-oe-expression', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='expression', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='field', ctx=Load()),
                                attr='readonly',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='data-oe-readonly', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                            value=Constant(value=' value_to_html(value, field, options=None)\n\n        Converts a single value to its HTML version/output\n        :rtype: unicode\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='escape', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pycompat', ctx=Load()),
                                            attr='to_text',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
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
                    name='record_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
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
                            value=Constant(value=' record_to_html(record, field_name, options)\n\n        Converts the specified field of the ``record`` to HTML\n\n        :rtype: unicode\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='record', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Subscript(
                                value=Name(id='record', ctx=Load()),
                                slice=Name(id='field_name', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='value', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=False, kind=None)],
                                ),
                                body=Constant(value=False, kind=None),
                                orelse=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_name',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='value_to_html',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='value', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='options',
                                            value=Name(id='options', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[
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
                    name='user_lang',
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
                            value=Constant(value=" user_lang()\n\n        Fetches the res.lang record corresponding to the language code stored\n        in the user's context.\n\n        :returns: Model[res.lang]\n        ", kind=None),
                        ),
                        Return(
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
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='IntegerConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.integer', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Integer', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
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
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='to_text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_lang',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='%d', kind=None),
                                                    Name(id='value', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='grouping',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='-', kind=None),
                                            Constant(value='-\ufeff', kind=None),
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
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='FloatConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.float', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Float', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='FloatConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_options',
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
                                    value=Name(id='options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='precision',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='integer', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Rounding precision', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='options', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='decimal_precision', kind=None),
                                ops=[In()],
                                comparators=[Name(id='options', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='precision', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='decimal.precision', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='precision_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='decimal_precision', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='precision', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='options', ctx=Load()),
                                        slice=Constant(value='precision', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='precision', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fmt', ctx=Store())],
                                    value=Constant(value='%f', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='float_utils', ctx=Load()),
                                            attr='float_round',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Name(id='precision', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fmt', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='%.{precision}f', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='precision',
                                                value=Name(id='precision', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='formatted', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_lang',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fmt', ctx=Load()),
                                            Name(id='value', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='grouping',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-', kind=None),
                                    Constant(value='-\ufeff', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='precision', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='formatted', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='(?:(0|\\d+?)0+)$', kind=None),
                                            Constant(value='\\1', kind=None),
                                            Name(id='formatted', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='to_text',
                                    ctx=Load(),
                                ),
                                args=[Name(id='formatted', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
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
                    name='record_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='precision', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='options', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='decimal_precision', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='options', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='_', ctx=Store()),
                                                Name(id='precision', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='field_name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_digits',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='options', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='options', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision',
                                                value=Name(id='precision', ctx=Load()),
                                            ),
                                        ],
                                    ),
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
                                        args=[
                                            Name(id='FloatConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='record_to_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='DateConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.date', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Date', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='DateConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_options',
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
                                    value=Name(id='options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='format',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='string', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Date format', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='options', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
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
                                func=Name(id='format_date', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    Name(id='value', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='date_format',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='options', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='format', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='DateTimeConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.datetime', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Datetime', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='DateTimeConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_options',
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
                                    value=Name(id='options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='format',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='string', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Pattern to format', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='tz_name',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='char', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Optional timezone name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='time_only',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='boolean', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Display only the time', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='hide_seconds',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='boolean', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Hide seconds', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='date_only',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='boolean', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Display only the date', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='options', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
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
                                operand=Name(id='value', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='options', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='options', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_lang',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='locale', ctx=Store())],
                            value=Call(
                                func=Name(id='babel_locale_parse', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='lang', ctx=Load()),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='format_func', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='babel', ctx=Load()),
                                    attr='dates',
                                    ctx=Load(),
                                ),
                                attr='format_datetime',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='context_timestamp',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='value', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tz_name', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tzinfo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='babel', ctx=Load()),
                                                attr='dates',
                                                ctx=Load(),
                                            ),
                                            attr='get_timezone',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='tz_name', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='tzinfo', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='format', kind=None),
                                ops=[In()],
                                comparators=[Name(id='options', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pattern', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='options', ctx=Load()),
                                        slice=Constant(value='format', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='time_only', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='strftime_pattern', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='lang', ctx=Load()),
                                                    attr='time_format',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='date_only', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='strftime_pattern', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='%s', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='lang', ctx=Load()),
                                                            attr='date_format',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='strftime_pattern', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='%s %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='lang', ctx=Load()),
                                                                    attr='date_format',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='lang', ctx=Load()),
                                                                    attr='time_format',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='pattern', ctx=Store())],
                                    value=Call(
                                        func=Name(id='posix_to_ldml', ctx=Load()),
                                        args=[Name(id='strftime_pattern', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='locale',
                                                value=Name(id='locale', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='hide_seconds', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pattern', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pattern', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=':ss', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=':s', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='time_only', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='format_func', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='babel', ctx=Load()),
                                            attr='dates',
                                            ctx=Load(),
                                        ),
                                        attr='format_time',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='pycompat', ctx=Load()),
                                            attr='to_text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='format_func', ctx=Load()),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='format',
                                                        value=Name(id='pattern', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='locale',
                                                        value=Name(id='locale', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='date_only', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='format_func', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='babel', ctx=Load()),
                                            attr='dates',
                                            ctx=Load(),
                                        ),
                                        attr='format_date',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='pycompat', ctx=Load()),
                                            attr='to_text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='format_func', ctx=Load()),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='format',
                                                        value=Name(id='pattern', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='locale',
                                                        value=Name(id='locale', ctx=Load()),
                                                    ),
                                                ],
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
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='to_text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='format_func', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='format',
                                                value=Name(id='pattern', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='tzinfo',
                                                value=Name(id='tzinfo', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='locale',
                                                value=Name(id='locale', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TextConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.text', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Text', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                            value=Constant(value='\n        Escapes the value and converts newlines to br. This is bullshit.\n        ', kind=None),
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id='value', ctx=Load()),
                                body=Call(
                                    func=Name(id='nl2br', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='escape', ctx=Load()),
                                            args=[Name(id='value', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='SelectionConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.selection', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Selection', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SelectionConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_options',
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
                                    value=Name(id='options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='selection',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='selection', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Selection', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='By default the widget uses the field information', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='required',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='options', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
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
                                operand=Name(id='value', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='escape', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='pycompat', ctx=Load()),
                                                    attr='to_text',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='options', ctx=Load()),
                                                            slice=Constant(value='selection', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='value', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
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
                    name='record_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='selection', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='options', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='options', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='options', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='selection',
                                                value=Call(
                                                    func=Name(id='dict', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='_fields',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Name(id='field_name', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='get_description',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            slice=Constant(value='selection', kind=None),
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SelectionConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='record_to_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ManyToOneConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.many2one', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Many to One', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
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
                                operand=Name(id='value', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='display_name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='value', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='nl2br', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='escape', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ManyToManyConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.many2many', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb field many2many', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
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
                                operand=Name(id='value', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='text', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=', ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='value', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='display_name', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='nl2br', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='escape', ctx=Load()),
                                        args=[Name(id='text', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='HTMLConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.html', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field HTML', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                            targets=[Name(id='irQweb', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.qweb', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='etree', ctx=Load()),
                                        attr='fromstring',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        BinOp(
                                            left=Constant(value='<body>%s</body>', kind=None),
                                            op=Mod(),
                                            right=Name(id='value', ctx=Load()),
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='etree', ctx=Load()),
                                                attr='HTMLParser',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='encoding',
                                                    value=Constant(value='utf-8', kind=None),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='element', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='body', ctx=Load()),
                                    attr='iter',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='element', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attrib', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='element', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='attrib', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='irQweb', ctx=Load()),
                                                    attr='_post_processing_att',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='element', ctx=Load()),
                                                        attr='tag',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='attrib', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='options', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='template_options', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='element', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='clear',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='element', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='attrib', ctx=Load())],
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
                            value=Call(
                                func=Name(id='M', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='etree', ctx=Load()),
                                                attr='tostring',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='body', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='encoding',
                                                    value=Constant(value='unicode', kind=None),
                                                ),
                                                keyword(
                                                    arg='method',
                                                    value=Constant(value='html', kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Slice(
                                            lower=Constant(value=6, kind=None),
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=7, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ImageConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' ``image`` widget rendering, inserts a data:uri-using image tag in the\n    document. May be overridden by e.g. the website module to generate links\n    instead.\n\n    .. todo:: what happens if different output need different converters? e.g.\n              reports may need embedded images or FS links whereas website\n              needs website-aware\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.image', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Image', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                                    targets=[Name(id='image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='open',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='BytesIO', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='value', ctx=Load())],
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='image', ctx=Load()),
                                            attr='verify',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[Constant(value='Non-image binary fields can not be converted to HTML', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[Constant(value='Invalid image content', kind=None)],
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
                        Return(
                            value=Call(
                                func=Name(id='M', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='<img src="data:%s;base64,%s">', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='Image', ctx=Load()),
                                                        attr='MIME',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Attribute(
                                                        value=Name(id='image', ctx=Load()),
                                                        attr='format',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='value', ctx=Load()),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='ascii', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ImageUrlConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' ``image_url`` widget rendering, inserts an image tag in the\n    document.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.image_url', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Image', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field.image', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
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
                                func=Name(id='M', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='<img src="%s">', kind=None),
                                        op=Mod(),
                                        right=Name(id='value', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='MonetaryConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" ``monetary`` converter, has a mandatory option\n    ``display_currency`` only if field is not of type Monetary.\n    Otherwise, if we are in presence of a monetary field, the field definition must\n    have a currency_field attribute set.\n\n    The currency is used for formatting *and rounding* of the float value. It\n    is assumed that the linked res_currency has a non-empty rounding value and\n    res.currency's ``round`` method is used to perform rounding.\n\n    .. note:: the monetary converter internally adds the qweb context to its\n              options mapping, so that the context is available to callees.\n              It's set under the ``_values`` key.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.monetary', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Monetary', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MonetaryConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_options',
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
                                    value=Name(id='options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='from_currency',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='model', kind=None),
                                                ),
                                                keyword(
                                                    arg='params',
                                                    value=Constant(value='res.currency', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Original currency', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='display_currency',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='model', kind=None),
                                                ),
                                                keyword(
                                                    arg='params',
                                                    value=Constant(value='res.currency', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Display currency', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='required',
                                                    value=Constant(value='value_to_html', kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='date',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='date', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Date', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Date used for the original currency (only used for t-esc). by default use the current date.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='model', kind=None),
                                                ),
                                                keyword(
                                                    arg='params',
                                                    value=Constant(value='res.company', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Company', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Company used for the original currency (only used for t-esc). By default use the user company', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='options', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                            targets=[Name(id='display_currency', ctx=Store())],
                            value=Subscript(
                                value=Name(id='options', ctx=Load()),
                                slice=Constant(value='display_currency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='value', ctx=Load()),
                                        Tuple(
                                            elts=[
                                                Name(id='int', ctx=Load()),
                                                Name(id='float', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The value send to monetary field is not a number.', kind=None)],
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
                        Assign(
                            targets=[Name(id='fmt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='%.{0}f', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='display_currency', ctx=Load()),
                                        attr='decimal_places',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='from_currency', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='date', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='date', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='today',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='company_id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='company_id', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='company', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.company', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='company_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='company', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='from_currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_convert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='value', ctx=Load()),
                                            Name(id='display_currency', ctx=Load()),
                                            Name(id='company', ctx=Load()),
                                            Name(id='date', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_lang',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='formatted_amount', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='lang', ctx=Load()),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='fmt', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='display_currency', ctx=Load()),
                                                            attr='round',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='grouping',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='monetary',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=' ', kind=None),
                                            Constant(value='\xa0', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-', kind=None),
                                    Constant(value='-\ufeff', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='pre', ctx=Store()),
                                Name(id='post', ctx=Store()),
                            ],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='display_currency', ctx=Load()),
                                    attr='position',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='before', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pre', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='{symbol}\xa0', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='symbol',
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='display_currency', ctx=Load()),
                                                            attr='symbol',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='post', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='\xa0{symbol}', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='symbol',
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='display_currency', ctx=Load()),
                                                            attr='symbol',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='label_price', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sep', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='lang', ctx=Load()),
                                        attr='decimal_point',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='integer_part', ctx=Store()),
                                                Name(id='decimal_part', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='formatted_amount', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sep', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='integer_part', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='sep', ctx=Load()),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='M', ctx=Load()),
                                                args=[Constant(value='{pre}<span class="oe_currency_value">{0}</span><span class="oe_currency_value" style="font-size:0.5em">{1}</span>{post}', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='integer_part', ctx=Load()),
                                            Name(id='decimal_part', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='pre',
                                                value=Name(id='pre', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='post',
                                                value=Name(id='post', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='M', ctx=Load()),
                                        args=[Constant(value='{pre}<span class="oe_currency_value">{0}</span>{post}', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='formatted_amount', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='pre',
                                        value=Name(id='pre', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='post',
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
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
                    name='record_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='options', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='options', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='display_currency', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='monetary', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='get_currency_field',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='record', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='display_currency', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Call(
                                            func=Attribute(
                                                value=Name(id='field', ctx=Load()),
                                                attr='get_currency_field',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='record', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='display_currency', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='currency_fields', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='k', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='k', ctx=Store()),
                                                        Name(id='v', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Name(id='fields', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='v', ctx=Load()),
                                                                    attr='type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='many2one', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='v', ctx=Load()),
                                                                    attr='comodel_name',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='res.currency', kind=None)],
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
                                If(
                                    test=Name(id='currency_fields', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='options', ctx=Load()),
                                                    slice=Constant(value='display_currency', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Subscript(
                                                    value=Name(id='currency_fields', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='date', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='options', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='date', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='date', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='company_id', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='options', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='company_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='company_id', kind=None)],
                                        keywords=[],
                                    ),
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
                                        args=[
                                            Name(id='MonetaryConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='record_to_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='TIMEDELTA_UNITS', ctx=Store())],
            value=Tuple(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='year', kind=None),
                            Call(
                                func=Name(id='_lt', ctx=Load()),
                                args=[Constant(value='year', kind=None)],
                                keywords=[],
                            ),
                            BinOp(
                                left=BinOp(
                                    left=Constant(value=3600, kind=None),
                                    op=Mult(),
                                    right=Constant(value=24, kind=None),
                                ),
                                op=Mult(),
                                right=Constant(value=365, kind=None),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='month', kind=None),
                            Call(
                                func=Name(id='_lt', ctx=Load()),
                                args=[Constant(value='month', kind=None)],
                                keywords=[],
                            ),
                            BinOp(
                                left=BinOp(
                                    left=Constant(value=3600, kind=None),
                                    op=Mult(),
                                    right=Constant(value=24, kind=None),
                                ),
                                op=Mult(),
                                right=Constant(value=30, kind=None),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='week', kind=None),
                            Call(
                                func=Name(id='_lt', ctx=Load()),
                                args=[Constant(value='week', kind=None)],
                                keywords=[],
                            ),
                            BinOp(
                                left=BinOp(
                                    left=Constant(value=3600, kind=None),
                                    op=Mult(),
                                    right=Constant(value=24, kind=None),
                                ),
                                op=Mult(),
                                right=Constant(value=7, kind=None),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='day', kind=None),
                            Call(
                                func=Name(id='_lt', ctx=Load()),
                                args=[Constant(value='day', kind=None)],
                                keywords=[],
                            ),
                            BinOp(
                                left=Constant(value=3600, kind=None),
                                op=Mult(),
                                right=Constant(value=24, kind=None),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='hour', kind=None),
                            Call(
                                func=Name(id='_lt', ctx=Load()),
                                args=[Constant(value='hour', kind=None)],
                                keywords=[],
                            ),
                            Constant(value=3600, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='minute', kind=None),
                            Call(
                                func=Name(id='_lt', ctx=Load()),
                                args=[Constant(value='minute', kind=None)],
                                keywords=[],
                            ),
                            Constant(value=60, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='second', kind=None),
                            Call(
                                func=Name(id='_lt', ctx=Load()),
                                args=[Constant(value='second', kind=None)],
                                keywords=[],
                            ),
                            Constant(value=1, kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='FloatTimeConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' ``float_time`` converter, to display integral or fractional values as\n    human-readable time spans (e.g. 1.5 as "01:30").\n\n    Can be used on any numerical field.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.float_time', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Float Time', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
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
                                func=Name(id='format_duration', ctx=Load()),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='DurationConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' ``duration`` converter, to display integral or fractional values as\n    human-readable time spans (e.g. 1.5 as "1 hour 30 minutes").\n\n    Can be used on any numerical field.\n\n    Has an option ``unit`` which can be one of ``second``, ``minute``,\n    ``hour``, ``day``, ``week`` or ``year``, used to interpret the numerical\n    field value before converting it. By default use ``second``.\n\n    Has an option ``round``. By default use ``second``.\n\n    Has an option ``digital`` to display 01:00 instead of 1 hour\n\n    Sub-second values will be ignored.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.duration', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Duration', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='DurationConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_options',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='unit', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Name(id='value', ctx=Load()),
                                        Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='label', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='value', ctx=Store()),
                                                Name(id='label', ctx=Store()),
                                                Name(id='ratio', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Name(id='TIMEDELTA_UNITS', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='digital',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='boolean', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Digital formatting', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='unit',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='selection', kind=None),
                                                ),
                                                keyword(
                                                    arg='params',
                                                    value=Name(id='unit', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Date unit', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Date unit used for comparison and formatting', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value='second', kind=None),
                                                ),
                                                keyword(
                                                    arg='required',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='round',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='selection', kind=None),
                                                ),
                                                keyword(
                                                    arg='params',
                                                    value=Name(id='unit', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Rounding unit', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="Date unit used for the rounding. The value must be smaller than 'hour' if you use the digital formatting.", kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value='second', kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='format',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='selection', kind=None),
                                                ),
                                                keyword(
                                                    arg='params',
                                                    value=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='long', kind=None),
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Long', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='short', kind=None),
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Short', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='narrow', kind=None),
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Narrow', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Format', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Formatting: long, short, narrow (not used for digital)', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value='long', kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='add_direction',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='boolean', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Add direction', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Add directional information (not used for digital)', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='options', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                            targets=[Name(id='units', ctx=Store())],
                            value=DictComp(
                                key=Name(id='unit', ctx=Load()),
                                value=Name(id='duration', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='unit', ctx=Store()),
                                                Name(id='label', ctx=Store()),
                                                Name(id='duration', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Name(id='TIMEDELTA_UNITS', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='locale', ctx=Store())],
                            value=Call(
                                func=Name(id='babel_locale_parse', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_lang',
                                                ctx=Load(),
                                            ),
                                            args=[],
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
                            targets=[Name(id='factor', ctx=Store())],
                            value=Subscript(
                                value=Name(id='units', ctx=Load()),
                                slice=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='unit', kind=None),
                                        Constant(value='second', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='round_to', ctx=Store())],
                            value=Subscript(
                                value=Name(id='units', ctx=Load()),
                                slice=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='round', kind=None),
                                        Constant(value='second', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='digital', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Name(id='round_to', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=3600, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='round_to', ctx=Store())],
                                    value=Constant(value=3600, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='round', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=BinOp(
                                                left=Name(id='value', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='factor', ctx=Load()),
                                            ),
                                            op=Div(),
                                            right=Name(id='round_to', ctx=Load()),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Mult(),
                                right=Name(id='round_to', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sections', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='digital', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='unit', ctx=Store()),
                                            Name(id='label', ctx=Store()),
                                            Name(id='secs_per_unit', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='TIMEDELTA_UNITS', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='secs_per_unit', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=3600, kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='v', ctx=Store()),
                                                        Name(id='r', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='divmod', ctx=Load()),
                                                args=[
                                                    Name(id='r', ctx=Load()),
                                                    Name(id='secs_per_unit', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='v', ctx=Load()),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='secs_per_unit', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='factor', ctx=Load())],
                                                            ),
                                                            Compare(
                                                                left=Name(id='secs_per_unit', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[Name(id='round_to', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='sections', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='sections', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=':', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sections', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='%02.0f', kind=None),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='round', ctx=Load()),
                                                                    args=[Name(id='v', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sections', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='value', ctx=Load()),
                                ops=[Lt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='r', ctx=Store())],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Name(id='r', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sections', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='-', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='unit', ctx=Store()),
                                    Name(id='label', ctx=Store()),
                                    Name(id='secs_per_unit', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='TIMEDELTA_UNITS', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='v', ctx=Store()),
                                                Name(id='r', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='divmod', ctx=Load()),
                                        args=[
                                            Name(id='r', ctx=Load()),
                                            Name(id='secs_per_unit', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='v', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='section', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='babel', ctx=Load()),
                                                attr='dates',
                                                ctx=Load(),
                                            ),
                                            attr='format_timedelta',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='v', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='secs_per_unit', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='granularity',
                                                value=Name(id='round_to', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='add_direction',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='options', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='add_direction', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='format',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='options', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='format', kind=None),
                                                        Constant(value='long', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='threshold',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='locale',
                                                value=Name(id='locale', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='section', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sections', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='section', ctx=Load())],
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
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sections', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='RelativeDatetimeConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.relative', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Relative', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='RelativeDatetimeConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_options',
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
                                    value=Name(id='options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='now',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='datetime', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Reference date', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Date to compare with the field value, by default use the current date.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='options', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                            targets=[Name(id='locale', ctx=Store())],
                            value=Call(
                                func=Name(id='babel_locale_parse', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_lang',
                                                ctx=Load(),
                                            ),
                                            args=[],
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
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='options', ctx=Load()),
                                        slice=Constant(value='now', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='to_text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='babel', ctx=Load()),
                                                attr='dates',
                                                ctx=Load(),
                                            ),
                                            attr='format_timedelta',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='value', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='reference', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='add_direction',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='locale',
                                                value=Name(id='locale', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
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
                    name='record_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='now', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='options', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='options', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='options', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='now',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='_fields',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='field_name', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
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
                                        args=[
                                            Name(id='RelativeDatetimeConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='record_to_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='BarcodeConverter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' ``barcode`` widget rendering, inserts a data:uri-using image tag in the\n    document. May be overridden by e.g. the website module to generate links\n    instead.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.barcode', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Barcode', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='BarcodeConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_options',
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
                                    value=Name(id='options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='symbology',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='string', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Barcode symbology', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Barcode type, eg: UPCA, EAN13, Code128', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value='Code128', kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='width',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='integer', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Width', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value=600, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='height',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='integer', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Height', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value=100, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='humanreadable',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='integer', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Human Readable', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='quiet',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='integer', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Constant(value='Quiet', kind=None),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='mask',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='string', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Constant(value='Mask', kind=None),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value='', kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='options', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='value', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='barcode_symbology', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='symbology', kind=None),
                                    Constant(value='Code128', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='barcode', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='barcode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='barcode_symbology', ctx=Load()),
                                    Name(id='value', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=DictComp(
                                            key=Name(id='key', ctx=Load()),
                                            value=Name(id='value', ctx=Load()),
                                            generators=[
                                                comprehension(
                                                    target=Tuple(
                                                        elts=[
                                                            Name(id='key', ctx=Store()),
                                                            Name(id='value', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='options', ctx=Load()),
                                                            attr='items',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    ifs=[
                                                        Compare(
                                                            left=Name(id='key', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='width', kind=None),
                                                                        Constant(value='height', kind=None),
                                                                        Constant(value='humanreadable', kind=None),
                                                                        Constant(value='quiet', kind=None),
                                                                        Constant(value='mask', kind=None),
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
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='img_element', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='img', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='k', ctx=Store()),
                                    Name(id='v', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='k', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='img_', kind=None)],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='k', ctx=Load()),
                                                    slice=Slice(
                                                        lower=Constant(value=4, kind=None),
                                                        upper=None,
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='safe_attrs', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='img_element', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='k', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Constant(value=4, kind=None),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='v', ctx=Load()),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='img_element', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='alt', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='img_element', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='alt', kind=None),
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Barcode %s', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Name(id='value', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='img_element', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='src', kind=None),
                                    BinOp(
                                        left=Constant(value='data:image/png;base64,%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='base64', ctx=Load()),
                                                        attr='b64encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='barcode', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='decode',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='M', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='html', ctx=Load()),
                                            attr='tostring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='img_element', ctx=Load())],
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
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Contact',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.contact', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Contact', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field.many2one', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_options',
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
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Contact', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_options',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contact_fields', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='field_name', kind=None),
                                            Constant(value='label', kind=None),
                                            Constant(value='default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='name', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Name', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='field_name', kind=None),
                                            Constant(value='label', kind=None),
                                            Constant(value='default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='address', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Address', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='field_name', kind=None),
                                            Constant(value='label', kind=None),
                                            Constant(value='default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='phone', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Phone', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='field_name', kind=None),
                                            Constant(value='label', kind=None),
                                            Constant(value='default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='mobile', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Mobile', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='field_name', kind=None),
                                            Constant(value='label', kind=None),
                                            Constant(value='default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='email', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Email', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='field_name', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='vat', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='VAT', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='separator_params', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='type',
                                        value=Constant(value='selection', kind=None),
                                    ),
                                    keyword(
                                        arg='selection',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value=' ', kind=None),
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Space', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Constant(value=',', kind=None),
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Comma', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Constant(value='-', kind=None),
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Dash', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Constant(value='|', kind=None),
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Vertical bar', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Constant(value='/', kind=None),
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Slash', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='placeholder',
                                        value=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Linebreak', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='array', kind=None),
                                                ),
                                                keyword(
                                                    arg='params',
                                                    value=Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='type',
                                                                value=Constant(value='selection', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='params',
                                                                value=Name(id='contact_fields', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Displayed fields', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='List of contact fields to display in the widget', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=ListComp(
                                                        elt=Call(
                                                            func=Attribute(
                                                                value=Name(id='param', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='field_name', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='param', ctx=Store()),
                                                                iter=Name(id='contact_fields', ctx=Load()),
                                                                ifs=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='param', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='default', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='separator',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='selection', kind=None),
                                                ),
                                                keyword(
                                                    arg='params',
                                                    value=Name(id='separator_params', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Address separator', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Separator use to split the address from the display_name.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_value',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='no_marker',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='boolean', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Hide badges', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="Don't display the font awesome marker", kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='no_tag_br',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='boolean', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Use comma', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Use comma instead of the <br> tag to display the address', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='phone_icons',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='boolean', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Display phone icons', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Display the phone icons even if no_marker is True', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='country_image',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='type',
                                                    value=Constant(value='boolean', kind=None),
                                                ),
                                                keyword(
                                                    arg='string',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Display country image', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='description',
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Display the country image if the field is present on the record', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='options', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
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
                    name='value_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
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
                                operand=Name(id='value', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='opf', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='fields', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='address', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='mobile', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sep', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='separator', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='template_options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='template_options', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='sep', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='opsep', ctx=Store())],
                                    value=Call(
                                        func=Name(id='escape', ctx=Load()),
                                        args=[Name(id='sep', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='template_options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='no_tag_br', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='opsep', ctx=Store())],
                                            value=Call(
                                                func=Name(id='escape', ctx=Load()),
                                                args=[Constant(value=', ', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='opsep', ctx=Store())],
                                            value=Call(
                                                func=Name(id='M', ctx=Load()),
                                                args=[Constant(value='<br/>', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='value', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='show_address',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name_get', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='value', ctx=Load()),
                                            attr='name_get',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='elem', ctx=Load()),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='elem', ctx=Store()),
                                                iter=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='name_get', ctx=Load()),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='\n', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=Slice(
                                                        lower=Constant(value=1, kind=None),
                                                        upper=None,
                                                        step=None,
                                                    ),
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
                            body=[
                                Assign(
                                    targets=[Name(id='address', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='opsep', ctx=Load()),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='name_get', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='\n', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=Slice(
                                                            lower=Constant(value=1, kind=None),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='address', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='val', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='address', kind=None),
                                    Constant(value='phone', kind=None),
                                    Constant(value='mobile', kind=None),
                                    Constant(value='city', kind=None),
                                    Constant(value='country_id', kind=None),
                                    Constant(value='website', kind=None),
                                    Constant(value='email', kind=None),
                                    Constant(value='vat', kind=None),
                                    Constant(value='vat_label', kind=None),
                                    Constant(value='fields', kind=None),
                                    Constant(value='object', kind=None),
                                    Constant(value='options', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='name_get', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='\n', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='address', ctx=Load()),
                                    Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='phone',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='mobile',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='city',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='value', ctx=Load()),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='vat',
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='value', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='vat_label',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='VAT', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Name(id='opf', ctx=Load()),
                                    Name(id='value', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.qweb', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='base.contact', kind=None),
                                    Name(id='val', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='template_options', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='QwebView',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.qweb', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field qweb', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field.many2one', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='record_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
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
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='view', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='view', ctx=Load()),
                                    attr='_name',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='ir.ui.view', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="%s.%s must be a 'ir.ui.view', got %r.", kind=None),
                                            Name(id='record', ctx=Load()),
                                            Name(id='field_name', ctx=Load()),
                                            Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='view', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='values', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='engine',
                                        value=Constant(value='ir.qweb', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
