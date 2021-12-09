Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccountTourUploadBill',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account.tour.upload.bill', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Account tour upload bill', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='attachment_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='ir.attachment', kind=None),
                            ),
                            keyword(
                                arg='relation',
                                value=Constant(value='account_tour_upload_bill_ir_attachments_rel', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Attachments', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='selection', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_selection_values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='sample', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='preview_invoice', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_preview_invoice', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Invoice Preview', kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_preview_invoice',
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
                            targets=[Name(id='invoice_date', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='fields', ctx=Load()),
                                            attr='Date',
                                            ctx=Load(),
                                        ),
                                        attr='today',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='days',
                                            value=Constant(value=12, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='addr', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='x', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=List(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='street',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='street2',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Constant(value=' ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        ListComp(
                                                            elt=Name(id='x', ctx=Load()),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='x', ctx=Store()),
                                                                    iter=List(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='env',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='company',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='state_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='env',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='company',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='zip',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    ifs=[Name(id='x', ctx=Load())],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ifs=[Name(id='x', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='INV/%s/0001', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='invoice_date', ctx=Load()),
                                        attr='strftime',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='%Y/%m', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
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
                                        args=[Constant(value='account.bill_preview', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='company_name', kind=None),
                                            Constant(value='company_street_address', kind=None),
                                            Constant(value='invoice_name', kind=None),
                                            Constant(value='invoice_ref', kind=None),
                                            Constant(value='invoice_date', kind=None),
                                            Constant(value='invoice_due_date', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Name(id='addr', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Invoice ', kind=None),
                                                op=Add(),
                                                right=Name(id='ref', ctx=Load()),
                                            ),
                                            Name(id='ref', ctx=Load()),
                                            Name(id='invoice_date', ctx=Load()),
                                            BinOp(
                                                left=Name(id='invoice_date', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=30, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='preview_invoice',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='html', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_selection_values',
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
                            targets=[Name(id='journal_alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.journal', kind=None),
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
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='purchase', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='sample', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Try a sample vendor bill', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='upload', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Upload your own bill', kind=None)],
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='journal_alias', ctx=Load()),
                                        attr='alias_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='journal_alias', ctx=Load()),
                                        attr='alias_domain',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='email', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Or send a bill to %s@%s', kind=None),
                                                            Attribute(
                                                                value=Name(id='journal_alias', ctx=Load()),
                                                                attr='alias_name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='journal_alias', ctx=Load()),
                                                                attr='alias_domain',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
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
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_action_list_view_bill',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bill_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[List(elts=[], ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='context', ctx=Load()),
                                    slice=Constant(value='default_move_type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='in_invoice', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='views', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Generated Documents', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='bill_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='tree,form', kind=None),
                                    Constant(value='account.move', kind=None),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Name(id='context', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='apply',
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_context',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='active_model', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='account.journal', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='active_ids', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='purchase_journal', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.journal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='active_ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='purchase_journal', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.journal', kind=None),
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
                                                            Constant(value='type', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='purchase', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='selection',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='upload', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='purchase_journal', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='default_journal_id',
                                                        value=Attribute(
                                                            value=Name(id='purchase_journal', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='default_move_type',
                                                        value=Constant(value='in_invoice', kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='create_invoice_from_attachment',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='attachment_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='attachment_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='selection',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='sample', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='bodies', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.actions.report', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_prepare_html',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='preview_invoice',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='sample_pdf', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.actions.report', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_run_wkhtmltopdf',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='bodies', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='invoice_date', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='fields', ctx=Load()),
                                                            attr='Date',
                                                            ctx=Load(),
                                                        ),
                                                        attr='today',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=12, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='attachment', ctx=Store())],
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
                                                            Constant(value='type', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='res_model', kind=None),
                                                            Constant(value='datas', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='binary', kind=None),
                                                            BinOp(
                                                                left=Constant(value='INV-%s-0001.pdf', kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='invoice_date', ctx=Load()),
                                                                        attr='strftime',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='%Y-%m', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            Constant(value='mail.compose.message', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='base64', ctx=Load()),
                                                                    attr='encodebytes',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='sample_pdf', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.partner', kind=None),
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
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='Deco Addict', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='limit',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='partner', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='partner', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.partner', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='is_company', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Deco Addict', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='bill', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.move', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='move_type', kind=None),
                                                            Constant(value='partner_id', kind=None),
                                                            Constant(value='ref', kind=None),
                                                            Constant(value='invoice_date', kind=None),
                                                            Constant(value='invoice_date_due', kind=None),
                                                            Constant(value='journal_id', kind=None),
                                                            Constant(value='invoice_line_ids', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='in_invoice', kind=None),
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=Constant(value='INV/%s/0001', kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='invoice_date', ctx=Load()),
                                                                        attr='strftime',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='%Y/%m', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            Name(id='invoice_date', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='invoice_date', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='timedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='days',
                                                                            value=Constant(value=30, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='purchase_journal', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='Command', ctx=Load()),
                                                                            attr='create',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='name', kind=None),
                                                                                    Constant(value='quantity', kind=None),
                                                                                    Constant(value='price_unit', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Constant(value='[FURN_8999] Three-Seat Sofa', kind=None),
                                                                                    Constant(value=5, kind=None),
                                                                                    Constant(value=1500, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='Command', ctx=Load()),
                                                                            attr='create',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='name', kind=None),
                                                                                    Constant(value='quantity', kind=None),
                                                                                    Constant(value='price_unit', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Constant(value='[FURN_8220] Four Person Desk', kind=None),
                                                                                    Constant(value=5, kind=None),
                                                                                    Constant(value=2350, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
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
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='bill', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='no_new_invoice',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='attachment_ids',
                                                        value=List(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='attachment', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_action_list_view_bill',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='bill', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='email_alias', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s@%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='purchase_journal', ctx=Load()),
                                                            attr='alias_name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='purchase_journal', ctx=Load()),
                                                            attr='alias_domain',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='new_wizard', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.tour.upload.bill.email.confirm', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='email_alias', kind=None)],
                                                        values=[Name(id='email_alias', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='view_id', ctx=Store())],
                                            value=Attribute(
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
                                                    args=[Constant(value='account.account_tour_upload_bill_email_confirm', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Dict(
                                                keys=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='view_mode', kind=None),
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='target', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='views', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='ir.actions.act_window', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Confirm', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='form', kind=None),
                                                    Constant(value='account.tour.upload.bill.email.confirm', kind=None),
                                                    Constant(value='new', kind=None),
                                                    Attribute(
                                                        value=Name(id='new_wizard', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Name(id='view_id', ctx=Load()),
                                                                    Constant(value='form', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
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
            name='AccountTourUploadBillEmailConfirm',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account.tour.upload.bill.email.confirm', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Account tour upload bill email confirm', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email_alias', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='apply',
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
                            targets=[Name(id='purchase_journal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.journal', kind=None),
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
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='purchase', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bill_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='account.move', kind=None),
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
                                                        Constant(value='journal_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Attribute(
                                                            value=Name(id='purchase_journal', ctx=Load()),
                                                            attr='id',
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
                                attr='ids',
                                ctx=Load(),
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
                                        slice=Constant(value='account.tour.upload.bill', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_action_list_view_bill',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bill_ids', ctx=Load())],
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
