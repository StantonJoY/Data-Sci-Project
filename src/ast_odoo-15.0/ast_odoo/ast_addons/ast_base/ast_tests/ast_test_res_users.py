Module(
    body=[
        ImportFrom(
            module='odoo.addons.base.models.res_users',
            names=[
                alias(name='is_selection_groups', asname=None),
                alias(name='get_selection_groups', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='TransactionCase', asname=None),
                alias(name='Form', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestUsers',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_name_search',
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
                            value=Constant(value=' Check name_search on user. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='User', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Flad the Impaler', kind=None),
                                            Constant(value='vlad', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='like_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Wlad the Impaler', kind=None),
                                            Constant(value='vladi', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='other_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Nothing similar', kind=None),
                                            Constant(value='nothing similar', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='all_users', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='test_user', ctx=Load()),
                                    op=BitOr(),
                                    right=Name(id='like_user', ctx=Load()),
                                ),
                                op=BitOr(),
                                right=Name(id='other_user', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='name_search',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='vlad', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='operator',
                                        value=Constant(value='ilike', kind=None),
                                    ),
                                ],
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
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='User', ctx=Load()),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                GeneratorExp(
                                                    elt=Subscript(
                                                        value=Name(id='i', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='i', ctx=Store()),
                                                            iter=Name(id='res', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='all_users', ctx=Load()),
                                    ),
                                    Name(id='test_user', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='name_search',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='vlad', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='operator',
                                        value=Constant(value='not ilike', kind=None),
                                    ),
                                ],
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
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='User', ctx=Load()),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                GeneratorExp(
                                                    elt=Subscript(
                                                        value=Name(id='i', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='i', ctx=Store()),
                                                            iter=Name(id='res', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='all_users', ctx=Load()),
                                    ),
                                    Name(id='all_users', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='name_search',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='operator',
                                        value=Constant(value='ilike', kind=None),
                                    ),
                                ],
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
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='User', ctx=Load()),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                GeneratorExp(
                                                    elt=Subscript(
                                                        value=Name(id='i', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='i', ctx=Store()),
                                                            iter=Name(id='res', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='all_users', ctx=Load()),
                                    ),
                                    Name(id='all_users', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='name_search',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='operator',
                                        value=Constant(value='not ilike', kind=None),
                                    ),
                                ],
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
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='User', ctx=Load()),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                GeneratorExp(
                                                    elt=Subscript(
                                                        value=Name(id='i', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='i', ctx=Store()),
                                                            iter=Name(id='res', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='all_users', ctx=Load()),
                                    ),
                                    Name(id='User', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='name_search',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lad', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='operator',
                                        value=Constant(value='ilike', kind=None),
                                    ),
                                ],
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
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='User', ctx=Load()),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                GeneratorExp(
                                                    elt=Subscript(
                                                        value=Name(id='i', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='i', ctx=Store()),
                                                            iter=Name(id='res', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='all_users', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='test_user', ctx=Load()),
                                        op=BitOr(),
                                        right=Name(id='like_user', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='name_search',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lad', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='operator',
                                        value=Constant(value='not ilike', kind=None),
                                    ),
                                ],
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
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='User', ctx=Load()),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                GeneratorExp(
                                                    elt=Subscript(
                                                        value=Name(id='i', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='i', ctx=Store()),
                                                            iter=Name(id='res', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='all_users', ctx=Load()),
                                    ),
                                    Name(id='other_user', ctx=Load()),
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
                    name='test_user_partner',
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
                            value=Constant(value=' Check that the user partner is well created ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='User', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Partner', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Company', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Company', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='company_1', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Company', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='company_2', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='company_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bob Partner', kind=None),
                                            Attribute(
                                                value=Name(id='company_2', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='test_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='company_ids', kind=None),
                                            Constant(value='company_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='John Smith', kind=None),
                                            Constant(value='jsmith', kind=None),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='company_1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company_1', ctx=Load()),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='test_user', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The partner_id linked to a user should be created without any company_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='test_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='company_ids', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bob Smith', kind=None),
                                            Constant(value='bsmith', kind=None),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='company_1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company_1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
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
                                        value=Attribute(
                                            value=Name(id='test_user', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='company_1', ctx=Load()),
                                    Constant(value='If the partner_id of a user has already a company, it is replaced by the user company', kind=None),
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
                    name='test_change_user_company',
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
                            value=Constant(value=' Check the partner company update when the user company is changed ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='User', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Company', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='User', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='John Smith', kind=None),
                                            Constant(value='jsmith', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Company', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='company_1', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Company', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='company_2', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='test_user', ctx=Load()),
                                attr='company_ids',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Name(id='company_1', ctx=Load()),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='test_user', ctx=Load()),
                                attr='company_ids',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Name(id='company_2', ctx=Load()),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_user', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='company_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='company_1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='test_user', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='On user company change, if its partner_id has no company_id,the company_id of the partner_id shall NOT be updated', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='test_user', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='company_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='company_1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_user', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='company_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='company_2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                        value=Attribute(
                                            value=Name(id='test_user', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='company_2', ctx=Load()),
                                    Constant(value='On user company change, if its partner_id has already a company_id,the company_id of the partner_id shall be updated', kind=None),
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
        ClassDef(
            name='TestUsers2',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_reified_groups',
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
                            value=Constant(value=' The groups handler doesn\'t use the "real" view with pseudo-fields\n        during installation, so it always works (because it uses the normal\n        groups_id field).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='view',
                                        value=Constant(value='base.view_users_form', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='bob', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='login',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='bob', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='save',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
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
                                        args=[Constant(value='base.group_user', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='groups_id',
                                        ctx=Load(),
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
                    name='test_selection_groups',
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
                            targets=[Name(id='app', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.module.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Foo', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='group1', ctx=Store()),
                                        Name(id='group2', ctx=Store()),
                                        Name(id='group0', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.groups', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='category_id', kind=None),
                                            ],
                                            values=[
                                                Name(id='name', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='app', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='name', ctx=Store()),
                                                iter=Tuple(
                                                    elts=[
                                                        Constant(value='User', kind=None),
                                                        Constant(value='Manager', kind=None),
                                                        Constant(value='Visitor', kind=None),
                                                    ],
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='group1', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='group2', ctx=Load()),
                                        attr='id',
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
                                    attr='assertLess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='group2', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='group0', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='group2', ctx=Load()),
                                    attr='implied_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='group1', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='group1', ctx=Load()),
                                    attr='implied_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='group0', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='group0', ctx=Load()),
                                    op=Add(),
                                    right=Name(id='group1', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='group2', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fname', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='name', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='name', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='res.users', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='fields_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Name(id='is_selection_groups', ctx=Load()),
                                                                args=[Name(id='name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='group0', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Call(
                                                                        func=Name(id='get_selection_groups', ctx=Load()),
                                                                        args=[Name(id='name', ctx=Load())],
                                                                        keywords=[],
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='get_selection_groups', ctx=Load()),
                                        args=[Name(id='fname', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='groups', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='foo', kind=None),
                                            Constant(value='foo', kind=None),
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
                                    value=Name(id='user', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Name(id='fname', ctx=Load())],
                                        values=[
                                            Attribute(
                                                value=Name(id='group0', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='groups_id',
                                            ctx=Load(),
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='groups', ctx=Load()),
                                    ),
                                    Name(id='group0', ctx=Load()),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Name(id='fname', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='fname', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='group0', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Name(id='fname', ctx=Load())],
                                        values=[
                                            Attribute(
                                                value=Name(id='group1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='groups_id',
                                            ctx=Load(),
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='groups', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='group0', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='group1', ctx=Load()),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Name(id='fname', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='fname', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='group1', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Name(id='fname', ctx=Load())],
                                        values=[
                                            Attribute(
                                                value=Name(id='group2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='groups_id',
                                            ctx=Load(),
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='groups', ctx=Load()),
                                    ),
                                    Name(id='groups', ctx=Load()),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Name(id='fname', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='fname', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='group2', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
