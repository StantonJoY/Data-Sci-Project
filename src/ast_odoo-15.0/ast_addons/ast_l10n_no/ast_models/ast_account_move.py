Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='stdnum',
            names=[alias(name='luhn', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccountMove',
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
                    value=Constant(value='account.move', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_invoice_reference_no_invoice',
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
                            value=Constant(value=' This computes the reference based on the Odoo format.\n            We calculat reference using invoice number and\n            partner id and added control digit at last.\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_kid_number',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_invoice_reference_no_partner',
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
                            value=Constant(value=' This computes the reference based on the Odoo format.\n            We calculat reference using invoice number and\n            partner id and added control digit at last.\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_kid_number',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_kid_number',
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
                        Assign(
                            targets=[Name(id='invoice_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Name(id='i', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='i', ctx=Load()),
                                                                    attr='isdigit',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='zfill',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=7, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=BinOp(
                                left=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='zfill',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=7, kind=None)],
                                        keywords=[],
                                    ),
                                    slice=Slice(
                                        lower=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=7, kind=None),
                                        ),
                                        upper=None,
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='invoice_name', ctx=Load()),
                                    slice=Slice(
                                        lower=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=7, kind=None),
                                        ),
                                        upper=None,
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='ref', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='luhn', ctx=Load()),
                                        attr='calc_check_digit',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='ref', ctx=Load())],
                                    keywords=[],
                                ),
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
