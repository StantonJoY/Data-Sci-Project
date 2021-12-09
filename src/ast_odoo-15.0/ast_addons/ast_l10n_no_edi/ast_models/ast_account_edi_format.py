Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.account_edi_ubl_bis3.models.account_edi_format',
            names=[alias(name='COUNTRY_EAS', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccountEdiFormat',
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
                    value=Constant(value='account.edi.format', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_ubl',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' OVERRIDE so that the generic ubl parser does not parse BIS3 any longer.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='is_ubl', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_is_ubl',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='is_ubl', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_is_ehf_3',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='filename', ctx=Load()),
                                                Name(id='tree', ctx=Load()),
                                            ],
                                            keywords=[],
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
                FunctionDef(
                    name='_is_ehf_3',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ns', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_bis3_namespaces',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='{urn:oasis:names:specification:ubl:schema:xsd:Invoice-2}Invoice', kind=None)],
                                    ),
                                    Compare(
                                        left=Constant(value='peppol', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='findtext',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='./cbc:ProfileID', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='namespaces',
                                                        value=Name(id='ns', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='tree', ctx=Load()),
                                                attr='xpath',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value="./cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID[text()='Foretaksregisteret']", kind=None)],
                                            keywords=[
                                                keyword(
                                                    arg='namespaces',
                                                    value=Name(id='ns', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_bis3_get_extra_partner_domains',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='ehf_3', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ns', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_bis3_namespaces',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='bronnoysund', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='./cac:AccountingSupplierParty/cac:Party/cbc:EndpointID[@schemeID="0192"]/text()', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='ns', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='bronnoysund', ctx=Load()),
                                    body=[
                                        Return(
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='l10n_no_bronnoysund_number', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Subscript(
                                                                value=Name(id='bronnoysund', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
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
                                    attr='_bis3_get_extra_partner_domains',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tree', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_ehf_3_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_bis3_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner_vals', ctx=Store()),
                            iter=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='customer_vals', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='supplier_vals', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='partner_vals', ctx=Load()),
                                        slice=Constant(value='partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='NO', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='partner_vals', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='bis3_endpoint',
                                                        value=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='l10n_no_bronnoysund_number',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='bis3_endpoint_scheme',
                                                        value=Constant(value='0192', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_export_ehf_3',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='l10n_no_edi.export_ehf_3_invoice', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_ehf_3_values',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoice', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vat', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='commercial_partner_id',
                                    ctx=Load(),
                                ),
                                attr='vat',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml_name', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='ehf-%s%s%s.xml', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='vat', ctx=Load()),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                        IfExp(
                                            test=Name(id='vat', ctx=Load()),
                                            body=Constant(value='-', kind=None),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                attr='replace',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='/', kind=None),
                                                Constant(value='_', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='raw', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='mimetype', kind=None),
                                        ],
                                        values=[
                                            Name(id='xml_name', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='xml_content', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='account.move', kind=None),
                                            Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='application/xml', kind=None),
                                        ],
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
                    name='_check_move_configuration',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='errors', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_check_move_configuration',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='ehf_3', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='errors', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='supplier', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='partner_id',
                                    ctx=Load(),
                                ),
                                attr='commercial_partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='supplier', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='NO', kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='supplier', ctx=Load()),
                                            attr='l10n_no_bronnoysund_number',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The supplier %r must have a Bronnoysund company registry.', kind=None),
                                                    Attribute(
                                                        value=Name(id='supplier', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='supplier', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='NO', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='supplier', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='COUNTRY_EAS', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The supplier %r is from a country that is not supported for EHF (Bis3)', kind=None),
                                                    Attribute(
                                                        value=Name(id='supplier', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='customer', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='commercial_partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='customer', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='NO', kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='customer', ctx=Load()),
                                            attr='l10n_no_bronnoysund_number',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The customer %r must have a Bronnoysund company registry.', kind=None),
                                                    Attribute(
                                                        value=Name(id='customer', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='customer', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='NO', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='customer', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='COUNTRY_EAS', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The customer %r is from a country that is not supported for EHF (Bis3)', kind=None),
                                                    Attribute(
                                                        value=Name(id='customer', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='errors', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_compatible_with_journal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='journal', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='ehf_3', kind=None)],
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
                                            attr='_is_compatible_with_journal',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='journal', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='journal', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='sale', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='journal', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='NO', kind=None)],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post_invoice_edi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoices', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='ehf_3', kind=None)],
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
                                            attr='_post_invoice_edi',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoices', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Name(id='invoices', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_export_ehf_3',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[Name(id='invoice', ctx=Load())],
                                values=[
                                    Dict(
                                        keys=[Constant(value='attachment', kind=None)],
                                        values=[Name(id='attachment', ctx=Load())],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice_from_xml_tree',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
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
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='ehf_3', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_ehf_3',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='filename', ctx=Load()),
                                            Name(id='tree', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_decode_bis3',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tree', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move', kind=None),
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_create_invoice_from_xml_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
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
                    name='_update_invoice_from_xml_tree',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
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
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='ehf_3', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_ehf_3',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='filename', ctx=Load()),
                                            Name(id='tree', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_decode_bis3',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tree', ctx=Load()),
                                            Name(id='invoice', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
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
                                    attr='_update_invoice_from_xml_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
                                    Name(id='invoice', ctx=Load()),
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
