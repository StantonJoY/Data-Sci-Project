Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='MergePartnerAutomatic',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='base.partner.merge.automatic.wizard', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_log_merge_operation',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='src_partners', annotation=None, type_comment=None),
                            arg(arg='dst_partner', annotation=None, type_comment=None),
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
                                        args=[
                                            Name(id='MergePartnerAutomatic', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_log_merge_operation',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='src_partners', ctx=Load()),
                                    Name(id='dst_partner', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dst_partner', ctx=Load()),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=BinOp(
                                            left=Constant(value='%s %s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Merged with the following partners:', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Constant(value=', ', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=BinOp(
                                                                    left=Constant(value='%s <%s> (ID %s)', kind=None),
                                                                    op=Mod(),
                                                                    right=Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='p', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Name(id='p', ctx=Load()),
                                                                                        attr='email',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value='n/a', kind=None),
                                                                                ],
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='p', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='p', ctx=Store()),
                                                                        iter=Name(id='src_partners', ctx=Load()),
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
