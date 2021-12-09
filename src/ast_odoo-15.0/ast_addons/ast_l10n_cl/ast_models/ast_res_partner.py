Module(
    body=[
        Import(
            names=[alias(name='stdnum', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ResPartner',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sii_taxpayer_types', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='1', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='VAT Affected (1st Category)', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='2', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Fees Receipt Issuer (2nd category)', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='3', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='End Consumer', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='4', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Foreigner', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_cl_sii_taxpayer_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='_sii_taxpayer_types', ctx=Load()),
                            Constant(value='Taxpayer Type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='1 - VAT Affected (1st Category) (Most of the cases)\n2 - Fees Receipt Issuer (Applies to suppliers who issue fees receipt)\n3 - End consumer (only receipts)\n4 - Foreigner', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_commercial_fields',
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
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='_commercial_fields',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[Constant(value='l10n_cl_sii_taxpayer_type', kind=None)],
                                    ctx=Load(),
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
                    name='_format_vat_cl',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='identification_types', ctx=Store())],
                            value=List(
                                elts=[
                                    Attribute(
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
                                            args=[Constant(value='l10n_latam_base.it_vat', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
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
                                            args=[Constant(value='l10n_cl.it_RUT', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
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
                                            args=[Constant(value='l10n_cl.it_RUN', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.country', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='country_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='identification_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='l10n_latam.identification.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_latam_identification_type_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_country_is_chile', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='country', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='CL', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='identification_type', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='CL', kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='partner_country_is_chile', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='l10n_latam_identification_type_id', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='identification_types', ctx=Load())],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='vat', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='stdnum', ctx=Load()),
                                                                                attr='util',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='get_cc_module',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='cl', kind=None),
                                                                            Constant(value='vat', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='format',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='values', ctx=Load()),
                                                                        slice=Constant(value='vat', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='.', kind=None),
                                                            Constant(value='', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='CL', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='upper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='vat', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_format_dotted_vat_cl',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='vat_l', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vat', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='-', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='n_vat', ctx=Store()),
                                        Name(id='n_dv', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='vat_l', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='vat_l', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%s-%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Name(id='format', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[Name(id='n_vat', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Constant(value=',d', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='replace',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value=',', kind=None),
                                                Constant(value='.', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        Name(id='n_dv', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='vat', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='vat', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_format_vat_cl',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Name(id='field', ctx=Load()),
                                            ops=[In()],
                                            comparators=[Name(id='values', ctx=Load())],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field', ctx=Store()),
                                                iter=List(
                                                    elts=[
                                                        Constant(value='vat', kind=None),
                                                        Constant(value='l10n_latam_identification_type_id', kind=None),
                                                        Constant(value='country_id', kind=None),
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
                            body=[
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='vat_values', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='vat', kind=None),
                                                    Constant(value='l10n_latam_identification_type_id', kind=None),
                                                    Constant(value='country_id', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='vat', kind=None),
                                                            Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='vat',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='l10n_latam_identification_type_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='country_id', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='country_id',
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
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='vat', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_format_vat_cl',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='vat_values', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
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
