Module(
    body=[
        ImportFrom(
            module='odoo.addons.test_mail.tests.common',
            names=[
                alias(name='TestMailCommon', asname=None),
                alias(name='TestRecipients', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='users', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMailComposerMixin',
            bases=[
                Name(id='TestMailCommon', ctx=Load()),
                Name(id='TestRecipients', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                        args=[
                                            Name(id='TestMailComposerMixin', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_init_mail_gateway',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='mail_template',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='subject', kind=None),
                                            Constant(value='body_html', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Subject for {{ object.name }}', kind=None),
                                            Constant(value='<p>Body for <t t-out="object.name"/></p>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_content_sync',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.composer.mixin', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='template_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Invite', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mail_template',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='subject',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mail_template',
                                            ctx=Load(),
                                        ),
                                        attr='subject',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mail_template',
                                            ctx=Load(),
                                        ),
                                        attr='body_html',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='subject', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='_render_field',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='subject', kind=None),
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='subject', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='Subject for %s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='_render_field',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='body', kind=None),
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='body', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='<p>Body for %s</p>', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rendering',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.composer.mixin', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='description', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Invite', kind=None),
                                            Constant(value='Subject for {{ object.name }}', kind=None),
                                            Constant(value='<p>Content from <t t-out="user.name"/></p>', kind=None),
                                            Constant(value='<p>Description for <t t-esc="object.name"/></p>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='subject',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Subject for {{ object.name }}', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    Constant(value='<p>Content from <t t-out="user.name"/></p>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='subject', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='_render_field',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='subject', kind=None),
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='subject', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='Subject for %s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='_render_field',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='body', kind=None),
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='body', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='<p>Content from %s</p>', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='description', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='_render_field',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='description', kind=None),
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='description', ctx=Load()),
                                    Constant(value='<p>Description for Invite</p>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='mail_composer_mixin', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
