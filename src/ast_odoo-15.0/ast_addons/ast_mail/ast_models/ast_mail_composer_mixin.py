Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='MailComposerMixin',
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
                    value=Constant(value=' Mixin used to edit and render some fields used when sending emails or\n    notifications based on a mail template.\n\n    Main current purpose is to hide details related to subject and body computation\n    and rendering based on a mail.template. It also give the base tools to control\n    who is allowed to edit body, notably when dealing with templating language\n    like inline_template or qweb.\n\n    It is meant to evolve in a near future with upcoming support of qweb and fine\n    grain control of rendering access.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mail.composer.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='mail.render.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Mail Composer Mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='subject', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Subject', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_subject', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='body', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Contents', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_body', kind=None),
                            ),
                            keyword(
                                arg='render_engine',
                                value=Constant(value='qweb', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='sanitize',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='template_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mail.template', kind=None),
                            Constant(value='Mail Template', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Constant(value="[('model', '=', render_model)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_mail_template_editor', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is Editor', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_is_mail_template_editor', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='can_edit_body', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Can Edit Body', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_can_edit_body', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_subject',
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
                        For(
                            target=Name(id='composer_mixin', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='composer_mixin', ctx=Load()),
                                        attr='template_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='composer_mixin', ctx=Load()),
                                                    attr='subject',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='composer_mixin', ctx=Load()),
                                                    attr='template_id',
                                                    ctx=Load(),
                                                ),
                                                attr='subject',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='composer_mixin', ctx=Load()),
                                                    attr='subject',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='composer_mixin', ctx=Load()),
                                                            attr='subject',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='template_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_body',
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
                        For(
                            target=Name(id='composer_mixin', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='composer_mixin', ctx=Load()),
                                        attr='template_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='composer_mixin', ctx=Load()),
                                                    attr='body',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='composer_mixin', ctx=Load()),
                                                    attr='template_id',
                                                    ctx=Load(),
                                                ),
                                                attr='body_html',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='composer_mixin', ctx=Load()),
                                                    attr='body',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='composer_mixin', ctx=Load()),
                                                            attr='body',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='template_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_is_mail_template_editor',
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
                            targets=[Name(id='is_mail_template_editor', ctx=Store())],
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
                                            attr='is_admin',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
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
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='is_mail_template_editor',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='is_mail_template_editor', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends_context',
                                ctx=Load(),
                            ),
                            args=[Constant(value='uid', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_can_edit_body',
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
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='can_edit_body',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='is_mail_template_editor',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='template_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='template_id', kind=None),
                                Constant(value='is_mail_template_editor', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
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
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Render the given field on the given records.\n        This method bypass the rights when needed to\n        be able to render the template values in mass mode.\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='field', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_fields',
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
                                                args=[
                                                    Constant(value='The field %s does not exist on the model %s', kind=None),
                                                    Name(id='field', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_name',
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
                        Assign(
                            targets=[Name(id='composer_value', ctx=Store())],
                            value=Subscript(
                                value=Name(id='self', ctx=Load()),
                                slice=Name(id='field', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='template_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='is_mail_template_editor',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='MailComposerMixin', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_render_field',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field', ctx=Load()),
                                            Starred(
                                                value=Name(id='args', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='template_field', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='field', ctx=Load()),
                                    ops=[Eq()],
                                    comparators=[Constant(value='body', kind=None)],
                                ),
                                body=Constant(value='body_html', kind=None),
                                orelse=Name(id='field', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='template_field', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='template_id',
                                            ctx=Load(),
                                        ),
                                        attr='_fields',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='template_value', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_id',
                                    ctx=Load(),
                                ),
                                slice=Name(id='template_field', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='field', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='body', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sanitized_template_value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='html_sanitize',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template_value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='can_edit_body',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Name(id='composer_value', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='sanitized_template_value', ctx=Load()),
                                                            Name(id='template_value', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='body',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='template_id',
                                                    ctx=Load(),
                                                ),
                                                attr='body_html',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='super', ctx=Load()),
                                                        args=[
                                                            Name(id='MailComposerMixin', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='_render_field',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='field', ctx=Load()),
                                                    Starred(
                                                        value=Name(id='args', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='composer_value', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='template_value', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='super', ctx=Load()),
                                                        args=[
                                                            Name(id='MailComposerMixin', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='_render_field',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='field', ctx=Load()),
                                                    Starred(
                                                        value=Name(id='args', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailComposerMixin', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_render_field',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field', ctx=Load()),
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
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
