Module(
    body=[
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
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
        Expr(
            value=Constant(value='\naccount.move object: add support for Belgian structured communication\n', kind=None),
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
                    name='_get_invoice_reference_be_partner',
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
                            value=Constant(value=" This computes the reference based on the belgian national standard\n            “OGM-VCS”.\n            For instance, if an invoice is issued for the partner with internal\n            reference 'food buyer 654', the digits will be extracted and used as\n            the data. This will lead to a check number equal to 72 and the\n            reference will be '+++000/0000/65472+++'.\n            If no reference is set for the partner, its id in the database will\n            be used.\n        ", kind=None),
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
                        Assign(
                            targets=[Name(id='bbacomm', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='sub',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='\\D', kind=None),
                                                        Constant(value='', kind=None),
                                                        BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='partner_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='ref',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='', kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
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
                                            ],
                                        ),
                                        slice=Slice(
                                            lower=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=10, kind=None),
                                            ),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='rjust',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10, kind=None),
                                    Constant(value='0', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[Name(id='bbacomm', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mod', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BinOp(
                                        left=Name(id='base', ctx=Load()),
                                        op=Mod(),
                                        right=Constant(value=97, kind=None),
                                    ),
                                    Constant(value=97, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='+++%s/%s/%s%02d+++', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='bbacomm', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=3, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='bbacomm', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=3, kind=None),
                                                upper=Constant(value=7, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='bbacomm', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=7, kind=None),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Name(id='mod', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='reference', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_invoice_reference_be_invoice',
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
                            value=Constant(value=" This computes the reference based on the belgian national standard\n            “OGM-VCS”.\n            The data of the reference is the database id number of the invoice.\n            For instance, if an invoice is issued with id 654, the check number\n            is 72 so the reference will be '+++000/0000/65472+++'.\n        ", kind=None),
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
                        Assign(
                            targets=[Name(id='base', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bbacomm', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Name(id='base', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='rjust',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10, kind=None),
                                    Constant(value='0', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[Name(id='bbacomm', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mod', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BinOp(
                                        left=Name(id='base', ctx=Load()),
                                        op=Mod(),
                                        right=Constant(value=97, kind=None),
                                    ),
                                    Constant(value=97, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='+++%s/%s/%s%02d+++', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='bbacomm', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=3, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='bbacomm', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=3, kind=None),
                                                upper=Constant(value=7, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='bbacomm', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=7, kind=None),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Name(id='mod', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='reference', ctx=Load()),
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
