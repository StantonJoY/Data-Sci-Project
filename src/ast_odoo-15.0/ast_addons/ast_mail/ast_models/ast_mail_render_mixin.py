Module(
    body=[
        Import(
            names=[alias(name='babel', asname=None)],
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
        ImportFrom(
            module='lxml',
            names=[alias(name='html', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='markupsafe',
            names=[alias(name='Markup', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.qweb',
            names=[alias(name='QWebCodeFound', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='AccessError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='is_html_empty', asname=None),
                alias(name='safe_eval', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.rendering_tools',
            names=[
                alias(name='convert_inline_template_to_qweb', asname=None),
                alias(name='parse_inline_template', asname=None),
                alias(name='render_inline_template', asname=None),
                alias(name='template_env_globals', asname=None),
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
            name='format_date',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='date', annotation=None, type_comment=None),
                    arg(arg='pattern', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='format_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='env', ctx=Load()),
                                    Name(id='date', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='date_format',
                                        value=Name(id='pattern', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lang_code',
                                        value=Name(id='lang_code', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Attribute(
                                    value=Name(id='babel', ctx=Load()),
                                    attr='core',
                                    ctx=Load(),
                                ),
                                attr='UnknownLocaleError',
                                ctx=Load(),
                            ),
                            name=None,
                            body=[
                                Return(
                                    value=Name(id='date', ctx=Load()),
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
            name='format_datetime',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='dt', annotation=None, type_comment=None),
                    arg(arg='tz', annotation=None, type_comment=None),
                    arg(arg='dt_format', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value='medium', kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='format_datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='env', ctx=Load()),
                                    Name(id='dt', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=Name(id='tz', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='dt_format',
                                        value=Name(id='dt_format', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lang_code',
                                        value=Name(id='lang_code', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Attribute(
                                    value=Name(id='babel', ctx=Load()),
                                    attr='core',
                                    ctx=Load(),
                                ),
                                attr='UnknownLocaleError',
                                ctx=Load(),
                            ),
                            name=None,
                            body=[
                                Return(
                                    value=Name(id='dt', ctx=Load()),
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
            name='format_time',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='time', annotation=None, type_comment=None),
                    arg(arg='tz', annotation=None, type_comment=None),
                    arg(arg='time_format', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value='medium', kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='format_time',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='env', ctx=Load()),
                                    Name(id='time', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=Name(id='tz', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='time_format',
                                        value=Name(id='time_format', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lang_code',
                                        value=Name(id='lang_code', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Attribute(
                                    value=Name(id='babel', ctx=Load()),
                                    attr='core',
                                    ctx=Load(),
                                ),
                                attr='UnknownLocaleError',
                                ctx=Load(),
                            ),
                            name=None,
                            body=[
                                Return(
                                    value=Name(id='time', ctx=Load()),
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
        ClassDef(
            name='MailRenderMixin',
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
                    value=Constant(value='mail.render.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Mail Render Mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_unrestricted_rendering', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lang', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Language', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Optional translation language (ISO code) to select when sending out an email. If not set, the english version will be used. This should usually be a placeholder expression that provides the appropriate language, e.g. {{ object.partner_id.lang }}.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='render_model', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Rendering Model', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_render_model', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model_object_field', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model.fields', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Field', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Select target field from the related document model.\nIf it is a relationship field you will be able to select a target field at the destination of the relationship.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sub_object', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.model', kind=None),
                            Constant(value='Sub-model', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When a relationship field is selected as first field, this field shows the document model the relationship goes to.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sub_model_object_field', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.model.fields', kind=None),
                            Constant(value='Sub-field', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When a relationship field is selected as first field, this field lets you select the target field within the destination document model (sub-model).', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='null_value', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Default Value', kind=None)],
                        keywords=[
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Optional value to use if the target field is empty', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='copyvalue', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Placeholder Expression', kind=None)],
                        keywords=[
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Final placeholder expression, to be copy-pasted in the desired template field.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_render_model',
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
                            value=Constant(value=' Give the target model for rendering. Void by default as models\n        inheriting from ``mail.render.mixin`` should define how to find this\n        model. ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='render_model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_dynamic_placeholder',
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
                            value=Constant(value=' Generate the dynamic placeholder ', kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='model_object_field',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='model_object_field',
                                                ctx=Load(),
                                            ),
                                            attr='ttype',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='many2one', kind=None),
                                                    Constant(value='one2many', kind=None),
                                                    Constant(value='many2many', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='model', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.model', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='model_object_field',
                                                            ctx=Load(),
                                                        ),
                                                        attr='relation',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='model', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sub_object',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='sub_field_name', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sub_model_object_field',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='copyvalue',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_build_expression',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='model_object_field',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='sub_field_name', ctx=Load()),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='null_value',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
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
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sub_object',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sub_model_object_field',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='copyvalue',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_build_expression',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='model_object_field',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='null_value',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sub_object',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='copyvalue',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sub_model_object_field',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='null_value',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='model_object_field', kind=None),
                                Constant(value='sub_model_object_field', kind=None),
                                Constant(value='null_value', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_build_expression',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='sub_field_name', annotation=None, type_comment=None),
                            arg(arg='null_value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns a placeholder expression for use in a template field,\n        based on the values provided in the placeholder assistant.\n\n        :param field_name: main field name\n        :param sub_field_name: sub field name (M2O)\n        :param null_value: default value if the target value is empty\n        :return: final placeholder expression ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='expression', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='field_name', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='expression', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='{{ object.', kind=None),
                                        op=Add(),
                                        right=Name(id='field_name', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='sub_field_name', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='expression', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value='.', kind=None),
                                                op=Add(),
                                                right=Name(id='sub_field_name', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='null_value', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='expression', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value=" or '''%s'''", kind=None),
                                                op=Mod(),
                                                right=Name(id='null_value', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Name(id='expression', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=' }}', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='expression', ctx=Load()),
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
                    name='_valid_field_parameter',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='name', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='render_engine', kind=None),
                                                    Constant(value='render_options', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_valid_field_parameter',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        keywords=[],
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
                    name='_replace_local_links',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='html', annotation=None, type_comment=None),
                            arg(arg='base_url', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Replace local links by absolute links. It is required in various\n        cases, for example when sending emails on chatter or sending mass\n        mailings. It replaces\n\n         * href of links (mailto will not match the regex)\n         * src of images (base64 hardcoded data will not match the regex)\n         * styling using url like background-image: url\n\n        It is done using regex because it is shorten than using an html parser\n        to create a potentially complex soupe and hope to have a result that\n        has not been harmed.\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='html', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='html', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='wrapper', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='html', ctx=Load()),
                                        Name(id='Markup', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=Name(id='Markup', ctx=Load()),
                                orelse=Name(id='str', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='ustr',
                                    ctx=Load(),
                                ),
                                args=[Name(id='html', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='html', ctx=Load()),
                                    Name(id='Markup', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='wrapper', ctx=Store())],
                                    value=Name(id='Markup', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        FunctionDef(
                            name='_sub_relative2absolute',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='match', annotation=None, type_comment=None)],
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
                                        operand=Attribute(
                                            value=Name(id='_sub_relative2absolute', ctx=Load()),
                                            attr='base_url',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='_sub_relative2absolute', ctx=Load()),
                                                    attr='base_url',
                                                    ctx=Store(),
                                                ),
                                            ],
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
                                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='get_param',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='web.base.url', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='match', ctx=Load()),
                                                attr='group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=1, kind=None)],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='urls', ctx=Load()),
                                                attr='url_join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='_sub_relative2absolute', ctx=Load()),
                                                    attr='base_url',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='match', ctx=Load()),
                                                        attr='group',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=2, kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='_sub_relative2absolute', ctx=Load()),
                                    attr='base_url',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='base_url', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(<img(?=\\s)[^>]*\\ssrc=")(/[^/][^"]+)', kind=None),
                                    Name(id='_sub_relative2absolute', ctx=Load()),
                                    Name(id='html', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(<a(?=\\s)[^>]*\\shref=")(/[^/][^"]+)', kind=None),
                                    Name(id='_sub_relative2absolute', ctx=Load()),
                                    Name(id='html', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(<[^>]+\\bstyle="[^"]+\\burl\\(\'?)(/[^/\'][^\'")]+)', kind=None),
                                    Name(id='_sub_relative2absolute', ctx=Load()),
                                    Name(id='html', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='wrapper', ctx=Load()),
                                args=[Name(id='html', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_render_encapsulate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='layout_xmlid', annotation=None, type_comment=None),
                            arg(arg='html', annotation=None, type_comment=None),
                            arg(arg='add_context', annotation=None, type_comment=None),
                            arg(arg='context_record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='template', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='layout_xmlid', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_not_found',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='QWeb template %s not found when rendering encapsulation template.', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='layout_xmlid', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='record_name', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='context_record', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='context_record', ctx=Load()),
                                            attr='display_name',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='model_description', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='context_record', ctx=Load()),
                                        body=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.model', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='context_record', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='display_name',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='template_ctx', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='body', kind=None),
                                            Constant(value='record_name', kind=None),
                                            Constant(value='model_description', kind=None),
                                            Constant(value='company', kind=None),
                                            Constant(value='record', kind=None),
                                        ],
                                        values=[
                                            Name(id='html', ctx=Load()),
                                            Name(id='record_name', ctx=Load()),
                                            Name(id='model_description', ctx=Load()),
                                            IfExp(
                                                test=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='context_record', ctx=Load()),
                                                        Compare(
                                                            left=Constant(value='company_id', kind=None),
                                                            ops=[In()],
                                                            comparators=[Name(id='context_record', ctx=Load())],
                                                        ),
                                                    ],
                                                ),
                                                body=Subscript(
                                                    value=Name(id='context_record', ctx=Load()),
                                                    slice=Constant(value='company_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Name(id='context_record', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='add_context', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='template_ctx', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='add_context', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='html', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='template', ctx=Load()),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template_ctx', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='engine',
                                                value=Constant(value='ir.qweb', kind=None),
                                            ),
                                            keyword(
                                                arg='minimal_qcontext',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='html', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.render.mixin', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_replace_local_links',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='html', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='html', ctx=Load()),
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
                    name='_prepend_preview',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='html', annotation=None, type_comment=None),
                            arg(arg='preview', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prepare the email body before sending. Add the text preview at the\n        beginning of the mail. The preview text is displayed bellow the mail\n        subject of most mail client (gmail, outlook...).\n\n        :param html: html content for which we want to prepend a preview\n        :param preview: the preview to add before the html content\n        :return: html with preprended preview\n        ', kind=None),
                        ),
                        If(
                            test=Name(id='preview', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='preview', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='preview', ctx=Load()),
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
                            targets=[Name(id='preview_markup', ctx=Store())],
                            value=Call(
                                func=Name(id='convert_inline_template_to_qweb', ctx=Load()),
                                args=[Name(id='preview', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='preview', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='html_preview', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='Markup', ctx=Load()),
                                                args=[Constant(value='\n                <div style="display:none;font-size:1px;height:0px;width:0px;opacity:0;">\n                    {}\n                </div>\n            ', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='preview_markup', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='prepend_html_content',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='html', ctx=Load()),
                                            Name(id='html_preview', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='html', ctx=Load()),
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
                    name='_render_eval_context',
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
                            value=Constant(value=' Evaluation context used in all rendering engines. Contains\n\n          * ``user``: current user browse record;\n          * ``ctx```: current context;\n          * various formatting tools;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='render_context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='format_date', kind=None),
                                    Constant(value='format_datetime', kind=None),
                                    Constant(value='format_time', kind=None),
                                    Constant(value='format_amount', kind=None),
                                    Constant(value='format_duration', kind=None),
                                    Constant(value='user', kind=None),
                                    Constant(value='ctx', kind=None),
                                    Constant(value='is_html_empty', kind=None),
                                ],
                                values=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='date', annotation=None, type_comment=None),
                                                arg(arg='date_format', annotation=None, type_comment=None),
                                                arg(arg='lang_code', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[
                                                Constant(value=False, kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                        ),
                                        body=Call(
                                            func=Name(id='format_date', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                Name(id='date', ctx=Load()),
                                                Name(id='date_format', ctx=Load()),
                                                Name(id='lang_code', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='dt', annotation=None, type_comment=None),
                                                arg(arg='tz', annotation=None, type_comment=None),
                                                arg(arg='dt_format', annotation=None, type_comment=None),
                                                arg(arg='lang_code', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[
                                                Constant(value=False, kind=None),
                                                Constant(value=False, kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                        ),
                                        body=Call(
                                            func=Name(id='format_datetime', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                Name(id='dt', ctx=Load()),
                                                Name(id='tz', ctx=Load()),
                                                Name(id='dt_format', ctx=Load()),
                                                Name(id='lang_code', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='time', annotation=None, type_comment=None),
                                                arg(arg='tz', annotation=None, type_comment=None),
                                                arg(arg='time_format', annotation=None, type_comment=None),
                                                arg(arg='lang_code', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[
                                                Constant(value=False, kind=None),
                                                Constant(value=False, kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                        ),
                                        body=Call(
                                            func=Name(id='format_time', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                Name(id='time', ctx=Load()),
                                                Name(id='tz', ctx=Load()),
                                                Name(id='time_format', ctx=Load()),
                                                Name(id='lang_code', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='amount', annotation=None, type_comment=None),
                                                arg(arg='currency', annotation=None, type_comment=None),
                                                arg(arg='lang_code', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[Constant(value=False, kind=None)],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='format_amount',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                Name(id='amount', ctx=Load()),
                                                Name(id='currency', ctx=Load()),
                                                Name(id='lang_code', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='value', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='format_duration',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='value', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    Name(id='is_html_empty', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='render_context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='copy', ctx=Load()),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template_env_globals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='render_context', ctx=Load()),
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
                    name='_render_template_qweb',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template_src', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='add_context', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Render a raw QWeb template.\n\n        :param str template_src: raw QWeb template to render;\n        :param str model: see ``MailRenderMixin._render_template()``;\n        :param list res_ids: see ``MailRenderMixin._render_template()``;\n\n        :param dict add_context: additional context to give to renderer. It\n          allows to add or update values to base rendering context generated\n          by ``MailRenderMixin._render_eval_context()``;\n        :param dict options: options for rendering (not used currently);\n\n        :return dict: {res_id: string of rendered template based on record}\n\n        :notice: Experimental. Use at your own risks only.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res_ids', ctx=Load()),
                                    Constant(value='', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='template_src', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='results', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='variables', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_render_eval_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='add_context', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='variables', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='add_context', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='is_restricted', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_unrestricted_rendering',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='is_admin',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='mail.group_mail_template_editor', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='res_ids', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='variables', ctx=Load()),
                                            slice=Constant(value='object', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='record', ctx=Load()),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='render_result', ctx=Store())],
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
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='html', ctx=Load()),
                                                            attr='fragment_fromstring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='template_src', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='create_parent',
                                                                value=Constant(value='div', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='variables', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='raise_on_code',
                                                        value=Name(id='is_restricted', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='render_result', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='render_result', ctx=Load()),
                                                slice=Slice(
                                                    lower=Constant(value=5, kind=None),
                                                    upper=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=6, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='QWebCodeFound', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='group', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='mail.group_mail_template_editor', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='AccessError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='Only users belonging to the "%s" group can modify dynamic templates.', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='group', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
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
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Failed to render template : %s', kind=None),
                                                            Name(id='template_src', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='exc_info',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='Failed to render QWeb template : %s)', kind=None),
                                                                    Name(id='e', ctx=Load()),
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
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='results', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='render_result', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
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
                    name='_render_template_qweb_view',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template_src', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='add_context', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Render a QWeb template based on an ir.ui.view content.\n\n        In addition to the generic evaluation context available, some other\n        variables are added:\n          * ``object``: record based on which the template is rendered;\n\n        :param str template_src: source QWeb template. It should be a string\n          XmlID allowing to fetch an ``ir.ui.view``;\n        :param str model: see ``MailRenderMixin._render_template()``;\n        :param list res_ids: see ``MailRenderMixin._render_template()``;\n\n        :param dict add_context: additional context to give to renderer. It\n          allows to add or update values to base rendering context generated\n          by ``MailRenderMixin._render_eval_context()``;\n        :param dict options: options for rendering (not used currently);\n\n        :return dict: {res_id: string of rendered template based on record}\n        ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Name(id='r', ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='r', ctx=Store()),
                                                iter=Name(id='res_ids', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Template rendering should be called on a valid record IDs.', kind=None)],
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
                            targets=[Name(id='view', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template_src', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_not_found',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res_ids', ctx=Load()),
                                    Constant(value='', kind='u'),
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
                                    value=Name(id='results', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='variables', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_render_eval_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='add_context', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='variables', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='add_context', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='safe_eval', ctx=Load()),
                                    attr='check_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='variables', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='res_ids', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='variables', ctx=Load()),
                                            slice=Constant(value='object', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='record', ctx=Load()),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='render_result', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='view', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='variables', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='engine',
                                                        value=Constant(value='ir.qweb', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='minimal_qcontext',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Failed to render template : %s (%d)', kind=None),
                                                            Name(id='template_src', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='view', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='exc_info',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Failed to render template : %(xml_id)s (%(view_id)d)', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='xml_id',
                                                                        value=Name(id='template_src', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='view_id',
                                                                        value=Attribute(
                                                                            value=Name(id='view', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
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
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='results', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='render_result', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
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
                    name='_render_template_inline_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template_txt', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='add_context', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Render a string-based template on records given by a model and a list\n        of IDs, using inline_template.\n\n        In addition to the generic evaluation context available, some other\n        variables are added:\n          * ``object``: record based on which the template is rendered;\n\n        :param str template_txt: template text to render\n        :param str model: see ``MailRenderMixin._render_template()``;\n        :param list res_ids: see ``MailRenderMixin._render_template()``;\n\n        :param dict add_context: additional context to give to renderer. It\n          allows to add or update values to base rendering context generated\n          by ``MailRenderMixin._render_inline_template_eval_context()``;\n        :param dict options: options for rendering;\n\n        :return dict: {res_id: string of rendered template based on record}\n        ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Name(id='r', ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='r', ctx=Store()),
                                                iter=Name(id='res_ids', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Template rendering should be called on a valid record IDs.', kind=None)],
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
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res_ids', ctx=Load()),
                                    Constant(value='', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='template_txt', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='results', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='template_instructions', ctx=Store())],
                            value=Call(
                                func=Name(id='parse_inline_template', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Name(id='template_txt', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_dynamic', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='template_instructions', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='template_instructions', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_unrestricted_rendering',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Name(id='is_dynamic', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='is_admin',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='mail.group_mail_template_editor', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='group', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail.group_mail_template_editor', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Only users belonging to the "%s" group can modify dynamic templates.', kind=None),
                                                    Attribute(
                                                        value=Name(id='group', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='is_dynamic', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=DictComp(
                                        key=Name(id='record_id', ctx=Load()),
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='template_instructions', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='record_id', ctx=Store()),
                                                iter=Name(id='res_ids', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='variables', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_render_eval_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='add_context', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='variables', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='add_context', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='res_ids', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='variables', ctx=Load()),
                                            slice=Constant(value='object', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='record', ctx=Load()),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='results', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='render_inline_template', ctx=Load()),
                                                args=[
                                                    Name(id='template_instructions', ctx=Load()),
                                                    Name(id='variables', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Failed to render inline_template: \n%s', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='template_txt', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='exc_info',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='Failed to render inline_template template : %s)', kind=None),
                                                                    Name(id='e', ctx=Load()),
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
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
                    name='_render_template_postprocess',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rendered', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Tool method for post processing. In this method we ensure local\n        links ('/shop/Basil-1') are replaced by global links ('https://www.\n        mygarden.com/shop/Basil-1').\n\n        :param rendered: result of ``_render_template``;\n\n        :return dict: updated version of rendered per record ID;\n        ", kind=None),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='res_id', ctx=Store()),
                                    Name(id='rendered_html', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='rendered', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rendered', ctx=Load()),
                                            slice=Name(id='res_id', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_replace_local_links',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rendered_html', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='rendered', ctx=Load()),
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
                    name='_render_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template_src', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='engine', annotation=None, type_comment=None),
                            arg(arg='add_context', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='post_process', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='inline_template', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Render the given string on records designed by model / res_ids using\n        the given rendering engine. Possible engine are small_web, qweb, or\n        qweb_view.\n\n        :param str template_src: template text to render or xml id of a qweb view;\n        :param str model: model name of records on which we want to perform\n          rendering (aka 'crm.lead');\n        :param list res_ids: list of ids of records. All should belong to the\n          Odoo model given by model;\n        :param string engine: inline_template, qweb or qweb_view;\n\n        :param dict add_context: additional context to give to renderer. It\n          allows to add or update values to base rendering context generated\n          by ``MailRenderMixin._render_<engine>_eval_context()``;\n        :param dict options: options for rendering;\n        :param boolean post_process: perform a post processing on rendered result\n          (notably html links management). See``_render_template_postprocess``;\n\n        :return dict: {res_id: string of rendered template based on record}\n        ", kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='res_ids', ctx=Load()),
                                        Tuple(
                                            elts=[
                                                Name(id='list', ctx=Load()),
                                                Name(id='tuple', ctx=Load()),
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
                                                args=[Constant(value='Template rendering should be called only using on a list of IDs.', kind=None)],
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
                        If(
                            test=Compare(
                                left=Name(id='engine', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='inline_template', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='qweb_view', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Template rendering supports only inline_template, qweb, or qweb_view (view or raw).', kind=None)],
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
                        If(
                            test=Compare(
                                left=Name(id='engine', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='qweb_view', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rendered', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_render_template_qweb_view',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='template_src', ctx=Load()),
                                            Name(id='model', ctx=Load()),
                                            Name(id='res_ids', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='add_context',
                                                value=Name(id='add_context', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='options',
                                                value=Name(id='options', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='engine', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='qweb', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='rendered', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_render_template_qweb',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='template_src', ctx=Load()),
                                                    Name(id='model', ctx=Load()),
                                                    Name(id='res_ids', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='add_context',
                                                        value=Name(id='add_context', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='options',
                                                        value=Name(id='options', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='rendered', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_render_template_inline_template',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='template_src', ctx=Load()),
                                                    Name(id='model', ctx=Load()),
                                                    Name(id='res_ids', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='add_context',
                                                        value=Name(id='add_context', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='options',
                                                        value=Name(id='options', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='post_process', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='rendered', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_render_template_postprocess',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rendered', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='rendered', ctx=Load()),
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
                    name='_render_lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='engine', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='inline_template', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Given some record ids, return the lang for each record based on\n        lang field of template or through specific context-based key. Lang is\n        computed by performing a rendering on res_ids, based on self.render_model.\n\n        :param list res_ids: list of ids of records. All should belong to the\n          Odoo model given by model;\n        :param string engine: inline_template or qweb_view;\n\n        :return dict: {res_id: lang code (i.e. en_US)}\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='res_ids', ctx=Load()),
                                        Tuple(
                                            elts=[
                                                Name(id='list', ctx=Load()),
                                                Name(id='tuple', ctx=Load()),
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
                                                args=[Constant(value='Template rendering for language should be called with a list of IDs.', kind=None)],
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
                            targets=[Name(id='rendered_langs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_render_template',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='lang',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='render_model',
                                        ctx=Load(),
                                    ),
                                    Name(id='res_ids', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='engine',
                                        value=Name(id='engine', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='res_id', ctx=Load()),
                                                Name(id='lang', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='res_id', ctx=Store()),
                                                        Name(id='lang', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='rendered_langs', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
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
                FunctionDef(
                    name='_classify_per_lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='engine', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='inline_template', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Given some record ids, return for computed each lang a contextualized\n        template and its subset of res_ids.\n\n        :param list res_ids: list of ids of records (all belonging to same model\n          defined by self.render_model)\n        :param string engine: inline_template, qweb, or qweb_view;\n\n        :return dict: {lang: (template with lang=lang_code if specific lang computed\n          or template, res_ids targeted by that language}\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='template_preview_lang', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lang_to_res_ids', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='template_preview_lang', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[Name(id='res_ids', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='lang_to_res_ids', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='res_id', ctx=Store()),
                                            Name(id='lang', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_render_lang',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='res_ids', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='engine',
                                                        value=Name(id='engine', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='lang_to_res_ids', ctx=Load()),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='lang', ctx=Load()),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='res_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='lang', ctx=Load()),
                                                Tuple(
                                                    elts=[
                                                        IfExp(
                                                            test=Name(id='lang', ctx=Load()),
                                                            body=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='lang',
                                                                        value=Name(id='lang', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                            orelse=Name(id='self', ctx=Load()),
                                                        ),
                                                        Name(id='lang_res_ids', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='lang', ctx=Store()),
                                                        Name(id='lang_res_ids', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang_to_res_ids', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
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
                FunctionDef(
                    name='_render_field',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='engine', annotation=None, type_comment=None),
                            arg(arg='compute_lang', annotation=None, type_comment=None),
                            arg(arg='set_lang', annotation=None, type_comment=None),
                            arg(arg='add_context', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='post_process', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='inline_template', kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Given some record ids, render a template located on field on all\n        records. ``field`` should be a field of self (i.e. ``body_html`` on\n        ``mail.template``). res_ids are record IDs linked to ``model`` field\n        on self.\n\n        :param field: a field name existing on self;\n        :param list res_ids: list of ids of records (all belonging to same model\n          defined by ``self.render_model``)\n        :param string engine: inline_template, qweb, or qweb_view;\n\n        :param boolean compute_lang: compute language to render on translated\n          version of the template instead of default (probably english) one.\n          Language will be computed based on ``self.lang``;\n        :param string set_lang: force language for rendering. It should be a\n          valid lang code matching an activate res.lang. Checked only if\n          ``compute_lang`` is False;\n        :param dict add_context: additional context to give to renderer;\n        :param dict options: options for rendering;\n        :param boolean post_process: perform a post processing on rendered result\n          (notably html links management). See``_render_template_postprocess``);\n\n        :return dict: {res_id: string of rendered template based on record}\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='options', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='options', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='compute_lang', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='templates_res_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_classify_per_lang',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='set_lang', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='templates_res_ids', ctx=Store())],
                                            value=Dict(
                                                keys=[Name(id='set_lang', ctx=Load())],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='lang',
                                                                        value=Name(id='set_lang', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='res_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='templates_res_ids', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_context',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='lang', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='self', ctx=Load()),
                                                            Name(id='res_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='engine', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_fields',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='field', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Constant(value='render_engine', kind=None),
                                    Name(id='engine', ctx=Load()),
                                ],
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
                                        arg=None,
                                        value=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_fields',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='field', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                Constant(value='render_options', kind=None),
                                                Dict(keys=[], values=[]),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='post_process', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='post_process', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='post_process', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='res_id', ctx=Load()),
                                                Name(id='rendered', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='lang', ctx=Store()),
                                                        Tuple(
                                                            elts=[
                                                                Name(id='template', ctx=Store()),
                                                                Name(id='tpl_res_ids', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='templates_res_ids', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='res_id', ctx=Store()),
                                                        Name(id='rendered', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='template', ctx=Load()),
                                                                attr='_render_template',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='template', ctx=Load()),
                                                                    slice=Name(id='field', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='template', ctx=Load()),
                                                                    attr='render_model',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='tpl_res_ids', ctx=Load()),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='engine',
                                                                    value=Name(id='engine', ctx=Load()),
                                                                ),
                                                                keyword(
                                                                    arg='add_context',
                                                                    value=Name(id='add_context', ctx=Load()),
                                                                ),
                                                                keyword(
                                                                    arg='options',
                                                                    value=Name(id='options', ctx=Load()),
                                                                ),
                                                                keyword(
                                                                    arg='post_process',
                                                                    value=Name(id='post_process', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
