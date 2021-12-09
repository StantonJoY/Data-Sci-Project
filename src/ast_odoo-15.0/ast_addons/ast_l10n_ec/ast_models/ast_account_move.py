Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.l10n_ec.models.res_partner',
            names=[alias(name='verify_final_consumer', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_DOCUMENTS_MAPPING', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='01', kind=None),
                    Constant(value='02', kind=None),
                    Constant(value='03', kind=None),
                    Constant(value='04', kind=None),
                    Constant(value='05', kind=None),
                    Constant(value='06', kind=None),
                    Constant(value='07', kind=None),
                    Constant(value='09', kind=None),
                    Constant(value='20', kind=None),
                    Constant(value='21', kind=None),
                ],
                values=[
                    List(
                        elts=[
                            Constant(value='ec_dt_01', kind=None),
                            Constant(value='ec_dt_02', kind=None),
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_08', kind=None),
                            Constant(value='ec_dt_09', kind=None),
                            Constant(value='ec_dt_11', kind=None),
                            Constant(value='ec_dt_12', kind=None),
                            Constant(value='ec_dt_20', kind=None),
                            Constant(value='ec_dt_21', kind=None),
                            Constant(value='ec_dt_41', kind=None),
                            Constant(value='ec_dt_42', kind=None),
                            Constant(value='ec_dt_43', kind=None),
                            Constant(value='ec_dt_45', kind=None),
                            Constant(value='ec_dt_47', kind=None),
                            Constant(value='ec_dt_48', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='ec_dt_03', kind=None),
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_09', kind=None),
                            Constant(value='ec_dt_19', kind=None),
                            Constant(value='ec_dt_41', kind=None),
                            Constant(value='ec_dt_294', kind=None),
                            Constant(value='ec_dt_344', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='ec_dt_03', kind=None),
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_09', kind=None),
                            Constant(value='ec_dt_15', kind=None),
                            Constant(value='ec_dt_19', kind=None),
                            Constant(value='ec_dt_41', kind=None),
                            Constant(value='ec_dt_45', kind=None),
                            Constant(value='ec_dt_294', kind=None),
                            Constant(value='ec_dt_344', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_18', kind=None),
                            Constant(value='ec_dt_41', kind=None),
                            Constant(value='ec_dt_44', kind=None),
                            Constant(value='ec_dt_47', kind=None),
                            Constant(value='ec_dt_48', kind=None),
                            Constant(value='ec_dt_49', kind=None),
                            Constant(value='ec_dt_50', kind=None),
                            Constant(value='ec_dt_51', kind=None),
                            Constant(value='ec_dt_52', kind=None),
                            Constant(value='ec_dt_370', kind=None),
                            Constant(value='ec_dt_371', kind=None),
                            Constant(value='ec_dt_372', kind=None),
                            Constant(value='ec_dt_373', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_18', kind=None),
                            Constant(value='ec_dt_41', kind=None),
                            Constant(value='ec_dt_44', kind=None),
                            Constant(value='ec_dt_47', kind=None),
                            Constant(value='ec_dt_48', kind=None),
                            Constant(value='ec_dt_370', kind=None),
                            Constant(value='ec_dt_371', kind=None),
                            Constant(value='ec_dt_372', kind=None),
                            Constant(value='ec_dt_373', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_18', kind=None),
                            Constant(value='ec_dt_41', kind=None),
                            Constant(value='ec_dt_44', kind=None),
                            Constant(value='ec_dt_47', kind=None),
                            Constant(value='ec_dt_48', kind=None),
                            Constant(value='ec_dt_370', kind=None),
                            Constant(value='ec_dt_371', kind=None),
                            Constant(value='ec_dt_372', kind=None),
                            Constant(value='ec_dt_373', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_18', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='ec_dt_01', kind=None),
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_15', kind=None),
                            Constant(value='ec_dt_16', kind=None),
                            Constant(value='ec_dt_41', kind=None),
                            Constant(value='ec_dt_47', kind=None),
                            Constant(value='ec_dt_48', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='ec_dt_01', kind=None),
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_15', kind=None),
                            Constant(value='ec_dt_16', kind=None),
                            Constant(value='ec_dt_41', kind=None),
                            Constant(value='ec_dt_47', kind=None),
                            Constant(value='ec_dt_48', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='ec_dt_01', kind=None),
                            Constant(value='ec_dt_04', kind=None),
                            Constant(value='ec_dt_05', kind=None),
                            Constant(value='ec_dt_15', kind=None),
                            Constant(value='ec_dt_16', kind=None),
                            Constant(value='ec_dt_41', kind=None),
                            Constant(value='ec_dt_47', kind=None),
                            Constant(value='ec_dt_48', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
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
                Assign(
                    targets=[Name(id='l10n_ec_sri_payment_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='l10n_ec.sri.payment', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Payment Method (SRI)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_l10n_ec_identification_type',
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
                            targets=[Name(id='move', ctx=Store())],
                            value=Name(id='self', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='it_ruc', ctx=Store())],
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
                                args=[
                                    Constant(value='l10n_ec.ec_ruc', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='it_dni', ctx=Store())],
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
                                args=[
                                    Constant(value='l10n_ec.ec_dni', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='it_passport', ctx=Store())],
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
                                args=[
                                    Constant(value='l10n_ec.ec_passport', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_final_consumer', ctx=Store())],
                            value=Call(
                                func=Name(id='verify_final_consumer', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='commercial_partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='vat',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_ruc', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='commercial_partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='l10n_latam_identification_type_id',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='it_ruc', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_dni', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='commercial_partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='l10n_latam_identification_type_id',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='it_dni', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_passport', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='commercial_partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='l10n_latam_identification_type_id',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='it_passport', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='l10n_ec_is_exportation', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='commercial_partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='country_id',
                                        ctx=Load(),
                                    ),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='EC', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='identification_code', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='move', ctx=Load()),
                                    attr='move_type',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='in_invoice', kind=None),
                                            Constant(value='in_refund', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Name(id='is_ruc', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='identification_code', ctx=Store())],
                                            value=Constant(value='01', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Name(id='is_dni', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='identification_code', ctx=Store())],
                                                    value=Constant(value='02', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='identification_code', ctx=Store())],
                                                    value=Constant(value='03', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='move_type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Constant(value='out_refund', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='l10n_ec_is_exportation', ctx=Load()),
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='is_final_consumer', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='identification_code', ctx=Store())],
                                                            value=Constant(value='07', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Name(id='is_ruc', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='identification_code', ctx=Store())],
                                                                    value=Constant(value='04', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Name(id='is_dni', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='identification_code', ctx=Store())],
                                                                            value=Constant(value='05', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Name(id='is_passport', ctx=Load()),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='identification_code', ctx=Store())],
                                                                                    value=Constant(value='06', kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='is_ruc', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='identification_code', ctx=Store())],
                                                            value=Constant(value='20', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Name(id='is_dni', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='identification_code', ctx=Store())],
                                                                    value=Constant(value='21', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='identification_code', ctx=Store())],
                                                                    value=Constant(value='09', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='identification_code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_l10n_ec_documents_allowed',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='identification_code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='documents_allowed', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='l10n_latam.document.type', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='document_ref', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='_DOCUMENTS_MAPPING', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='identification_code', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='document_allowed', ctx=Store())],
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
                                        args=[
                                            BinOp(
                                                left=Constant(value='l10n_ec.%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='document_ref', ctx=Load()),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='document_allowed', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='documents_allowed', ctx=Store()),
                                            op=BitOr(),
                                            value=Name(id='document_allowed', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='documents_allowed', ctx=Load()),
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
                    name='_get_l10n_ec_internal_type',
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
                            targets=[Name(id='internal_type', ctx=Store())],
                            value=Call(
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
                                args=[
                                    Constant(value='internal_type', kind=None),
                                    Constant(value='invoice', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='move_type',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='out_refund', kind=None),
                                            Constant(value='in_refund', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='internal_type', ctx=Store())],
                                    value=Constant(value='credit_note', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='debit_origin_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='internal_type', ctx=Store())],
                                    value=Constant(value='debit_note', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='internal_type', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_l10n_latam_documents_domain',
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='journal_id',
                                                    ctx=Load(),
                                                ),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='account_fiscal_country_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
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
                                                args=[Constant(value='base.ec', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_latam_use_documents',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_get_l10n_latam_documents_domain',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='country_id.code', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='EC', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='internal_type', kind=None),
                                            Constant(value='in', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='invoice', kind=None),
                                                    Constant(value='debit_note', kind=None),
                                                    Constant(value='credit_note', kind=None),
                                                    Constant(value='invoice_in', kind=None),
                                                ],
                                                ctx=Load(),
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
                            targets=[Name(id='internal_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_l10n_ec_internal_type',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='allowed_documents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_l10n_ec_documents_allowed',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_l10n_ec_identification_type',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='internal_type', ctx=Load()),
                                    Name(id='allowed_documents', ctx=Load()),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='allowed_documents', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='x', ctx=Load()),
                                                                            attr='internal_type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='internal_type', ctx=Load())],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='domain', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_ec_formatted_sequence',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Constant(value='%s %s-%s-%09d', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='l10n_latam_document_type_id',
                                                ctx=Load(),
                                            ),
                                            attr='doc_code_prefix',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_ec_entity',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_ec_emission',
                                            ctx=Load(),
                                        ),
                                        Name(id='number', ctx=Load()),
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
                    name='_get_starting_sequence',
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
                            value=Constant(value='If use documents then will create a new starting sequence using the document type code prefix and the\n        journal document number with a 8 padding number', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Load(),
                                        ),
                                        attr='l10n_latam_use_documents',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='EC', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='l10n_latam_document_type_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_ec_formatted_sequence',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                                    attr='_get_starting_sequence',
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
                    name='_get_last_sequence_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='relaxed', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='l10n_latam_document_type_model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='l10n_latam.document.type', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='where_string', ctx=Store()),
                                        Name(id='param', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountMove', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_last_sequence_domain',
                                    ctx=Load(),
                                ),
                                args=[Name(id='relaxed', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='EC', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='l10n_latam_use_documents',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='move_type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Constant(value='out_refund', kind=None),
                                                    Constant(value='in_invoice', kind=None),
                                                    Constant(value='in_refund', kind=None),
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
                                        Tuple(
                                            elts=[
                                                Name(id='where_string', ctx=Store()),
                                                Name(id='param', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='AccountMove', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_get_last_sequence_domain',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=False, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='internal_type', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_l10n_ec_internal_type',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='document_types', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='l10n_latam_document_type_model', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='internal_type', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='internal_type', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='country_id.code', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='EC', kind=None),
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
                                If(
                                    test=Name(id='document_types', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='where_string', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value='\n                AND l10n_latam_document_type_id in %(l10n_latam_document_type_id)s\n                ', kind=None),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='param', ctx=Load()),
                                                    slice=Constant(value='l10n_latam_document_type_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='document_types', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
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
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='where_string', ctx=Load()),
                                    Name(id='param', ctx=Load()),
                                ],
                                ctx=Load(),
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
