Module(
    body=[
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='HrEmployee',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='hr.employee', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_barcodes_and_pin_hashed',
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
                        If(
                            test=UnaryOp(
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
                                    args=[Constant(value='point_of_sale.group_pos_user', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='visible_emp_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
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
                        Assign(
                            targets=[Name(id='employees_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='visible_emp_ids', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='barcode', kind=None),
                                            Constant(value='pin', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='e', ctx=Store()),
                            iter=Name(id='employees_data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='barcode', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='barcode', kind=None),
                                            ctx=Load(),
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='hashlib', ctx=Load()),
                                                        attr='sha1',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='e', ctx=Load()),
                                                                    slice=Constant(value='barcode', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='encode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='utf8', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='hexdigest',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='pin', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='pin', kind=None),
                                            ctx=Load(),
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='hashlib', ctx=Load()),
                                                        attr='sha1',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='e', ctx=Load()),
                                                                    slice=Constant(value='pin', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='encode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='utf8', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='hexdigest',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='employees_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_unlink_except_active_pos_session',
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
                            targets=[Name(id='configs_with_employees', ctx=Store())],
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
                                                slice=Constant(value='pos.config', kind=None),
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
                                                            Constant(value='module_pos_hr', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='True', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='c', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='current_session_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='configs_with_all_employees', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='configs_with_employees', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='c', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='c', ctx=Load()),
                                                attr='employee_ids',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='configs_with_specific_employees', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='configs_with_employees', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='c', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BinOp(
                                            left=Attribute(
                                                value=Name(id='c', ctx=Load()),
                                                attr='employee_ids',
                                                ctx=Load(),
                                            ),
                                            op=BitAnd(),
                                            right=Name(id='self', ctx=Load()),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='configs_with_all_employees', ctx=Load()),
                                    Name(id='configs_with_specific_employees', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='error_msg', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='You cannot delete an employee that may be used in an active PoS session, close the session(s) first: \n', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='employee', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='config_ids', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='configs_with_all_employees', ctx=Load()),
                                                op=BitOr(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='configs_with_specific_employees', ctx=Load()),
                                                        attr='filtered',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='c', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=Compare(
                                                                left=Name(id='employee', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='c', ctx=Load()),
                                                                        attr='employee_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='config_ids', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='error_msg', ctx=Store()),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Employee: %s - PoS Config(s): %s \n', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='employee', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Constant(value=', ', kind=None),
                                                                        attr='join',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        GeneratorExp(
                                                                            elt=Attribute(
                                                                                value=Name(id='config', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            generators=[
                                                                                comprehension(
                                                                                    target=Name(id='config', ctx=Store()),
                                                                                    iter=Name(id='config_ids', ctx=Load()),
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
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[Name(id='error_msg', ctx=Load())],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='ondelete',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='at_uninstall',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
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
