Module(
    body=[
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestIrDefault',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_defaults',
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
                            value=Constant(value=' check the mechanism of user-defined defaults ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='companyA', ctx=Store())],
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
                        Assign(
                            targets=[Name(id='companyB', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='companyA', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='CompanyB', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user1', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user1', ctx=Load()),
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
                                            Constant(value='u2', kind=None),
                                            Constant(value='u2', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user1', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='company_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='u3', kind=None),
                                            Constant(value='u3', kind=None),
                                            Attribute(
                                                value=Name(id='companyB', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='companyB', ctx=Load()),
                                                attr='ids',
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
                            targets=[Name(id='IrDefault1', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.default', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrDefault2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrDefault1', ctx=Load()),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user2', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrDefault3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrDefault1', ctx=Load()),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user3', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault1', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='field_id.model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='res.partner', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrDefault1', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='ref', kind=None),
                                    Constant(value='GLOBAL', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user_id',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault1', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='GLOBAL', kind=None)],
                                    ),
                                    Constant(value="Can't retrieve the created default value for all users.", kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault2', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='GLOBAL', kind=None)],
                                    ),
                                    Constant(value="Can't retrieve the created default value for all users.", kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault3', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='GLOBAL', kind=None)],
                                    ),
                                    Constant(value="Can't retrieve the created default value for all users.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrDefault1', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='ref', kind=None),
                                    Constant(value='COMPANY', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user_id',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault1', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='COMPANY', kind=None)],
                                    ),
                                    Constant(value="Can't retrieve the created default value for company.", kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault2', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='COMPANY', kind=None)],
                                    ),
                                    Constant(value="Can't retrieve the created default value for company.", kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault3', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='GLOBAL', kind=None)],
                                    ),
                                    Constant(value='Unexpected default value for company.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrDefault2', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='ref', kind=None),
                                    Constant(value='USER', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user_id',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault1', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='COMPANY', kind=None)],
                                    ),
                                    Constant(value="Can't retrieve the created default value for user.", kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault2', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='USER', kind=None)],
                                    ),
                                    Constant(value='Unexpected default value for user.', kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault3', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='GLOBAL', kind=None)],
                                    ),
                                    Constant(value='Unexpected default value for company.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='default1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='IrDefault1', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='default_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='ref', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ref', kind=None)],
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
                                    Name(id='default1', ctx=Load()),
                                    Constant(value='COMPANY', kind=None),
                                    Constant(value='Wrong default value.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='default2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='IrDefault2', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='default_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='ref', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ref', kind=None)],
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
                                    Name(id='default2', ctx=Load()),
                                    Constant(value='USER', kind=None),
                                    Constant(value='Wrong default value.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='default3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='IrDefault3', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='default_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='ref', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ref', kind=None)],
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
                                    Name(id='default3', ctx=Load()),
                                    Constant(value='GLOBAL', kind=None),
                                    Constant(value='Wrong default value.', kind=None),
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
                    name='test_conditions',
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
                            value=Constant(value=' check user-defined defaults with condition ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='IrDefault', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.default', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='field_id.model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='res.partner', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrDefault', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='ref', kind=None),
                                    Constant(value='X', kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='ref', kind=None)],
                                        values=[Constant(value='X', kind=None)],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='condition',
                                                value=Constant(value='name=Agrolait', kind=None),
                                            ),
                                        ],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='field_id.model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='res.partner.title', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrDefault', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner.title', kind=None),
                                    Constant(value='shortcut', kind=None),
                                    Constant(value='X', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrDefault', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner.title', kind=None),
                                    Constant(value='shortcut', kind=None),
                                    Constant(value='Mr', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='condition',
                                        value=Constant(value='name=Mister', kind=None),
                                    ),
                                ],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner.title', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='shortcut', kind=None)],
                                        values=[Constant(value='X', kind=None)],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner.title', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='condition',
                                                value=Constant(value='name=Miss', kind=None),
                                            ),
                                        ],
                                    ),
                                    Dict(keys=[], values=[]),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner.title', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='condition',
                                                value=Constant(value='name=Mister', kind=None),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[Constant(value='shortcut', kind=None)],
                                        values=[Constant(value='Mr', kind=None)],
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
                    name='test_invalid',
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
                            value=Constant(value=" check error cases with 'ir.default' ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='IrDefault', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.default', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='unknown_model', kind=None),
                                            Constant(value='unknown_field', kind=None),
                                            Constant(value=42, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='res.partner', kind=None),
                                            Constant(value='unknown_field', kind=None),
                                            Constant(value=42, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='res.partner', kind=None),
                                            Constant(value='lang', kind=None),
                                            Constant(value='some_LANG', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='res.partner', kind=None),
                                            Constant(value='credit_limit', kind=None),
                                            Constant(value='foo', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_removal',
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
                            value=Constant(value=' check defaults for many2one with their value being removed ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='IrDefault', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.default', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='field_id.model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='res.partner', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='title', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner.title', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='President', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrDefault', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='title', kind=None),
                                    Attribute(
                                        value=Name(id='title', ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='title', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='title', ctx=Load()),
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
                                    value=Name(id='title', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='get_model_defaults',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
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
                    name='test_multi_company_defaults',
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
                            value=Constant(value='Check defaults in multi-company environment.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='company_a', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='C_A', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_b', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='C_B', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_a_b', ctx=Store())],
                            value=BinOp(
                                left=Name(id='company_a', ctx=Load()),
                                op=Add(),
                                right=Name(id='company_b', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_b_a', ctx=Store())],
                            value=BinOp(
                                left=Name(id='company_b', ctx=Load()),
                                op=Add(),
                                right=Name(id='company_a', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='multi_company_user', ctx=Store())],
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
                                            Constant(value='company_id', kind=None),
                                            Constant(value='company_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='u2', kind=None),
                                            Constant(value='u2', kind=None),
                                            Attribute(
                                                value=Name(id='company_a', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company_a_b', ctx=Load()),
                                                attr='ids',
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
                            targets=[Name(id='IrDefault', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.default', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='multi_company_user', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='allowed_company_ids',
                                                value=Attribute(
                                                    value=Name(id='company_a', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='ref', kind=None),
                                    Constant(value='CADefault', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user_id',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrDefault', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='allowed_company_ids',
                                                value=Attribute(
                                                    value=Name(id='company_b', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='ref', kind=None),
                                    Constant(value='CBDefault', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user_id',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
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
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='IrDefault', ctx=Load()),
                                                attr='get_model_defaults',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='res.partner', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='ref', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='CADefault', kind=None),
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
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='IrDefault', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='allowed_company_ids',
                                                            value=Attribute(
                                                                value=Name(id='company_a', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                attr='get_model_defaults',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='res.partner', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='ref', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='CADefault', kind=None),
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
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='IrDefault', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='allowed_company_ids',
                                                            value=Attribute(
                                                                value=Name(id='company_b', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                attr='get_model_defaults',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='res.partner', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='ref', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='CBDefault', kind=None),
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
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='IrDefault', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='allowed_company_ids',
                                                            value=Attribute(
                                                                value=Name(id='company_a_b', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                attr='get_model_defaults',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='res.partner', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='ref', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='CADefault', kind=None),
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
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='IrDefault', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='allowed_company_ids',
                                                            value=Attribute(
                                                                value=Name(id='company_b_a', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                attr='get_model_defaults',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='res.partner', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='ref', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='CBDefault', kind=None),
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
