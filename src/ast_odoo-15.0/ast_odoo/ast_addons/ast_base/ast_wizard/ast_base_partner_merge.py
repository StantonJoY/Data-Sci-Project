Module(
    body=[
        ImportFrom(
            module='ast',
            names=[alias(name='literal_eval', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='ValidationError', asname=None),
                alias(name='UserError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Constant(value='odoo.addons.base.partner.merge', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='MergePartnerLine',
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
                    value=Constant(value='base.partner.merge.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Merge Partner Line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='min_id asc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='wizard_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='base.partner.merge.automatic.wizard', kind=None),
                            Constant(value='Wizard', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='min_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='MinID', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='aggr_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Ids', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
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
                Expr(
                    value=Constant(value='\n        The idea behind this wizard is to create a list of potential partners to\n        merge. We use two objects, the first one is the wizard for the end-user.\n        And the second will contain the partner list to merge.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='base.partner.merge.automatic.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Merge Partner Wizard', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
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
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='active_ids', ctx=Store())],
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
                                args=[Constant(value='active_ids', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
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
                                            args=[Constant(value='active_model', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='res.partner', kind=None)],
                                    ),
                                    Name(id='active_ids', ctx=Load()),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='state', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='state', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='selection', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='partner_ids', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='partner_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='active_ids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='dst_partner_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='dst_partner_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_ordered_partner',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='active_ids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    slice=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
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
                            value=Name(id='res', ctx=Load()),
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
                Assign(
                    targets=[Name(id='group_by_email', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Email', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_by_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Name', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_by_is_company', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is Company', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_by_vat', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='VAT', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_by_parent_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Parent Company', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='option', kind=None),
                                            Constant(value='Option', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='selection', kind=None),
                                            Constant(value='Selection', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='finished', kind=None),
                                            Constant(value='Finished', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='State', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='option', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='number_group', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Group of Contacts', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='current_line_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='base.partner.merge.line', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Current Line', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='base.partner.merge.line', kind=None),
                            Constant(value='wizard_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Lines', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Contacts', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dst_partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Destination Contact', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='exclude_contact', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='A user associated to the contact', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='exclude_journal_item', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Journal Items associated to the contact', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='maximum_group', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Maximum of Group of Contacts', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_fk_on',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='table', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" return a list of many2one relation with the given table.\n            :param table : the name of the sql table to return relations\n            :returns a list of tuple 'table name', 'column name'.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value="\n            SELECT cl1.relname as table, att1.attname as column\n            FROM pg_constraint as con, pg_class as cl1, pg_class as cl2, pg_attribute as att1, pg_attribute as att2\n            WHERE con.conrelid = cl1.oid\n                AND con.confrelid = cl2.oid\n                AND array_lower(con.conkey, 1) = 1\n                AND con.conkey[1] = att1.attnum\n                AND att1.attrelid = cl1.oid\n                AND cl2.relname = %s\n                AND att2.attname = 'id'\n                AND array_lower(con.confkey, 1) = 1\n                AND con.confkey[1] = att2.attnum\n                AND att2.attrelid = cl2.oid\n                AND con.contype = 'f'\n        ", kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='query', ctx=Load()),
                                    Tuple(
                                        elts=[Name(id='table', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
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
                    name='_update_foreign_keys',
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
                            value=Constant(value=' Update all foreign key from the src_partner to dst_partner. All many2one fields will be updated.\n            :param src_partners : merge source res.partner recordset (does not include destination one)\n            :param dst_partner : record of destination res.partner\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='_update_foreign_keys for dst_partner: %s for src_partners: %s', kind=None),
                                    Attribute(
                                        value=Name(id='dst_partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='src_partners', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                            targets=[Name(id='relations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_fk_on',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='res_partner', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='table', ctx=Store()),
                                    Name(id='column', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='relations', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='base_partner_merge_', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='table', ctx=Load())],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value="SELECT column_name FROM information_schema.columns WHERE table_name LIKE '%s'", kind=None),
                                        op=Mod(),
                                        right=Name(id='table', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='query', ctx=Load()),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='columns', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='data', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='fetchall',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='data', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='column', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='columns', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='query_dic', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='table', kind=None),
                                            Constant(value='column', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Name(id='table', ctx=Load()),
                                            Name(id='column', ctx=Load()),
                                            Subscript(
                                                value=Name(id='columns', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='columns', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[LtE()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='query', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='\n                    UPDATE "%(table)s" as ___tu\n                    SET "%(column)s" = %%s\n                    WHERE\n                        "%(column)s" = %%s AND\n                        NOT EXISTS (\n                            SELECT 1\n                            FROM "%(table)s" as ___tw\n                            WHERE\n                                "%(column)s" = %%s AND\n                                ___tu.%(value)s = ___tw.%(value)s\n                        )', kind=None),
                                                op=Mod(),
                                                right=Name(id='query_dic', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='partner', ctx=Store()),
                                            iter=Name(id='src_partners', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='execute',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='query', ctx=Load()),
                                                            Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='dst_partner', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='partner', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='dst_partner', ctx=Load()),
                                                                        attr='id',
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
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Try(
                                            body=[
                                                With(
                                                    items=[
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Name(id='mute_logger', ctx=Load()),
                                                                args=[Constant(value='odoo.sql_db', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            optional_vars=None,
                                                        ),
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='savepoint',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            optional_vars=None,
                                                        ),
                                                    ],
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='query', ctx=Store())],
                                                            value=BinOp(
                                                                left=Constant(value='UPDATE "%(table)s" SET "%(column)s" = %%s WHERE "%(column)s" IN %%s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='query_dic', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='execute',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='query', ctx=Load()),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='dst_partner', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Name(id='tuple', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='src_partners', ctx=Load()),
                                                                                        attr='ids',
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
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='column', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='Partner', ctx=Load()),
                                                                                attr='_parent_name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='table', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='res_partner', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='query', ctx=Store())],
                                                                    value=Constant(value='\n                                WITH RECURSIVE cycle(id, parent_id) AS (\n                                        SELECT id, parent_id FROM res_partner\n                                    UNION\n                                        SELECT  cycle.id, res_partner.parent_id\n                                        FROM    res_partner, cycle\n                                        WHERE   res_partner.id = cycle.parent_id AND\n                                                cycle.id != cycle.parent_id\n                                )\n                                SELECT id FROM cycle WHERE id = parent_id AND id = %s\n                            ', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='_cr',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='execute',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='query', ctx=Load()),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='dst_partner', ctx=Load()),
                                                                                        attr='id',
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
                                                    ],
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Attribute(
                                                        value=Name(id='psycopg2', ctx=Load()),
                                                        attr='Error',
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='query', ctx=Store())],
                                                            value=BinOp(
                                                                left=Constant(value='DELETE FROM "%(table)s" WHERE "%(column)s" IN %%s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='query_dic', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='execute',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='query', ctx=Load()),
                                                                    Tuple(
                                                                        elts=[
                                                                            Call(
                                                                                func=Name(id='tuple', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='src_partners', ctx=Load()),
                                                                                        attr='ids',
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
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    name='_update_reference_fields',
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
                            value=Constant(value=' Update all reference fields from the src_partner to dst_partner.\n            :param src_partners : merge source res.partner recordset (does not include destination one)\n            :param dst_partner : record of destination res.partner\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='_update_reference_fields for dst_partner: %s for src_partners: %r', kind=None),
                                    Attribute(
                                        value=Name(id='dst_partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='src_partners', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='update_records',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='model', annotation=None, type_comment=None),
                                    arg(arg='src', annotation=None, type_comment=None),
                                    arg(arg='field_model', annotation=None, type_comment=None),
                                    arg(arg='field_id', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value='model', kind=None),
                                    Constant(value='res_id', kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='Model', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='model', ctx=Load()),
                                            ops=[In()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='model', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=None, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='Model', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[Return(value=None)],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Model', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='field_model', ctx=Load()),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='res.partner', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Name(id='field_id', ctx=Load()),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='src', ctx=Load()),
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
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Name(id='mute_logger', ctx=Load()),
                                                        args=[Constant(value='odoo.sql_db', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='savepoint',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='records', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Name(id='field_id', ctx=Load())],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='dst_partner', ctx=Load()),
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
                                                            value=Name(id='records', ctx=Load()),
                                                            attr='flush',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='psycopg2', ctx=Load()),
                                                attr='Error',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='records', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='unlink',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='update_records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='functools', ctx=Load()),
                                    attr='partial',
                                    ctx=Load(),
                                ),
                                args=[Name(id='update_records', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='src_partners', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='update_records', ctx=Load()),
                                        args=[Constant(value='calendar', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='src',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='field_model',
                                                value=Constant(value='model_id.model', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='update_records', ctx=Load()),
                                        args=[Constant(value='ir.attachment', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='src',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='field_model',
                                                value=Constant(value='res_model', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='update_records', ctx=Load()),
                                        args=[Constant(value='mail.followers', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='src',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='field_model',
                                                value=Constant(value='res_model', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='update_records', ctx=Load()),
                                        args=[Constant(value='mail.activity', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='src',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='field_model',
                                                value=Constant(value='res_model', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='update_records', ctx=Load()),
                                        args=[Constant(value='mail.message', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='src',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='update_records', ctx=Load()),
                                        args=[Constant(value='ir.model.data', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='src',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.fields', kind=None),
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
                                                    Constant(value='ttype', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='reference', kind=None),
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
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='records', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='Model', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='model',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='field', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='Model', ctx=Load()),
                                                    attr='_fields',
                                                    ctx=Load(),
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='KeyError', ctx=Load()),
                                            name=None,
                                            body=[Continue()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='compute',
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='partner', ctx=Store()),
                                    iter=Name(id='src_partners', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='records_ref', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Model', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='=', kind=None),
                                                                    BinOp(
                                                                        left=Constant(value='res.partner,%d', kind=None),
                                                                        op=Mod(),
                                                                        right=Attribute(
                                                                            value=Name(id='partner', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
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
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='res.partner,%d', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='dst_partner', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='records_ref', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
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
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    name='_get_summable_fields',
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
                            value=Constant(value=' Returns the list of fields that should be summed when merging partners\n        ', kind=None),
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_values',
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
                            value=Constant(value=' Update values of dst_partner with the ones from the src_partners.\n            :param src_partners : recordset of source res.partner\n            :param dst_partner : record of destination res.partner\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='_update_values for dst_partner: %s for src_partners: %r', kind=None),
                                    Attribute(
                                        value=Name(id='dst_partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='src_partners', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dst_partner', ctx=Load()),
                                            attr='fields_get',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='keys',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='summable_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_summable_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='write_serializer',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='item', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='item', ctx=Load()),
                                            Attribute(
                                                value=Name(id='models', ctx=Load()),
                                                attr='BaseModel',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Name(id='item', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Name(id='item', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='column', ctx=Store()),
                            iter=Name(id='model_fields', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='field', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='dst_partner', ctx=Load()),
                                            attr='_fields',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='column', ctx=Load()),
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
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='many2many', kind=None),
                                                            Constant(value='one2many', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='item', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='itertools', ctx=Load()),
                                                    attr='chain',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='src_partners', ctx=Load()),
                                                    List(
                                                        elts=[Name(id='dst_partner', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Subscript(
                                                        value=Name(id='item', ctx=Load()),
                                                        slice=Name(id='column', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='column', ctx=Load()),
                                                                        ops=[In()],
                                                                        comparators=[Name(id='summable_fields', ctx=Load())],
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='column', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Subscript(
                                                                        value=Name(id='values', ctx=Load()),
                                                                        slice=Name(id='column', ctx=Load()),
                                                                        ctx=Store(),
                                                                    ),
                                                                    op=Add(),
                                                                    value=Call(
                                                                        func=Name(id='write_serializer', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='item', ctx=Load()),
                                                                                slice=Name(id='column', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            slice=Name(id='column', ctx=Load()),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Name(id='write_serializer', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='item', ctx=Load()),
                                                                                slice=Name(id='column', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='id', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='parent_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='parent_id', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dst_partner', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='parent_id', ctx=Load()),
                                    Compare(
                                        left=Name(id='parent_id', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='dst_partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='dst_partner', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='parent_id', kind=None)],
                                                        values=[Name(id='parent_id', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValidationError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Skip recursive partner hierarchies for parent_id %s of partner: %s', kind=None),
                                                            Name(id='parent_id', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='dst_partner', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
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
                    name='_merge',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner_ids', annotation=None, type_comment=None),
                            arg(arg='dst_partner', annotation=None, type_comment=None),
                            arg(arg='extra_checks', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' private implementation of merge partner\n            :param partner_ids : ids of partner to merge\n            :param dst_partner : record of destination res.partner\n            :param extra_checks: pass False to bypass extra sanity check (e.g. email address)\n        ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='is_admin',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='extra_checks', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                            targets=[Name(id='partner_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Partner', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='partner_ids', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Lt()],
                                comparators=[Constant(value=2, kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='partner_ids', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=3, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='For safety reasons, you cannot merge more than 3 contacts together. You can re-open the wizard several times if needed.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='child_ids', ctx=Store())],
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
                        For(
                            target=Name(id='partner_id', ctx=Store()),
                            iter=Name(id='partner_ids', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='child_ids', ctx=Store()),
                                    op=BitOr(),
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='Partner', ctx=Load()),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='id', kind=None),
                                                                Constant(value='child_of', kind=None),
                                                                List(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='partner_id', ctx=Load()),
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
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Name(id='partner_id', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BinOp(
                                left=Name(id='partner_ids', ctx=Load()),
                                op=BitAnd(),
                                right=Name(id='child_ids', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You cannot merge a contact with one of his parent.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='extra_checks', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='email',
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='partner', ctx=Store()),
                                                                    iter=Name(id='partner_ids', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='All contacts must have the same email. Only the Administrator can merge contacts with different emails.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='dst_partner', ctx=Load()),
                                    Compare(
                                        left=Name(id='dst_partner', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='partner_ids', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='src_partners', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='partner_ids', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='dst_partner', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='ordered_partners', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_ordered_partner',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='partner_ids', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='dst_partner', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='ordered_partners', ctx=Load()),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='src_partners', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='ordered_partners', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='dst_partner: %s', kind=None),
                                    Attribute(
                                        value=Name(id='dst_partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='extra_checks', ctx=Load()),
                                    Compare(
                                        left=Constant(value='account.move.line', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.move.line', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='partner_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            ListComp(
                                                                elt=Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='partner', ctx=Store()),
                                                                        iter=Name(id='src_partners', ctx=Load()),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
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
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Only the destination contact may be linked to existing Journal Items. Please ask the Administrator if you need to merge several contacts linked to existing Journal Items.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='dst_partner', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='partner_ids', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='user_ids', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='company_ids', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='link',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='dst_partner', ctx=Load()),
                                                                            attr='company_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='dst_partner', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_foreign_keys',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_reference_fields',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_values',
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
                                    value=Name(id='self', ctx=Load()),
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
                                    value=Name(id='src_partners', ctx=Load()),
                                    attr='unlink',
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(uid = %s) merged the partners %r with %s', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_uid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='src_partners', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='dst_partner', ctx=Load()),
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
                FunctionDef(
                    name='_generate_query',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='maximum_group', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=100, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Build the SQL query on res.partner table to group them according to given criteria\n            :param fields : list of column names to group by the partners\n            :param maximum_group : limit of the query\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sql_fields', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Name(id='fields', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='field', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sql_fields', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='lower(%s)', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='field', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='field', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[Constant(value='vat', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='sql_fields', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value="replace(%s, ' ', '')", kind=None),
                                                                op=Mod(),
                                                                right=Name(id='field', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='sql_fields', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='field', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=', ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sql_fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Name(id='fields', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='field', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='vat', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='filters', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='field', ctx=Load()),
                                                            Constant(value='IS NOT', kind=None),
                                                            Constant(value='NULL', kind=None),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='criteria', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' AND ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=BinOp(
                                            left=Constant(value='%s %s %s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Name(id='field', ctx=Load()),
                                                    Name(id='operator', ctx=Load()),
                                                    Name(id='value', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='field', ctx=Store()),
                                                        Name(id='operator', ctx=Store()),
                                                        Name(id='value', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Name(id='filters', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='text', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='SELECT min(id), array_agg(id)', kind=None),
                                    Constant(value='FROM res_partner', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='criteria', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='text', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='WHERE %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='criteria', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='text', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='GROUP BY %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='group_fields', ctx=Load()),
                                            ),
                                            Constant(value='HAVING COUNT(*) >= 2', kind=None),
                                            Constant(value='ORDER BY min(id)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='maximum_group', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='text', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='LIMIT %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='maximum_group', ctx=Load()),
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
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='text', ctx=Load())],
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
                    name='_compute_selected_groupby',
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
                            value=Constant(value=' Returns the list of field names the partner can be grouped (as merge\n            criteria) according to the option checked on the wizard\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_by_prefix', ctx=Store())],
                            value=Constant(value='group_by_', kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field_name', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_fields',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='field_name', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='group_by_prefix', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='field_name', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='groups', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='field_name', ctx=Load()),
                                                                slice=Slice(
                                                                    lower=Call(
                                                                        func=Name(id='len', ctx=Load()),
                                                                        args=[Name(id='group_by_prefix', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    upper=None,
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='groups', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You have to specify a filter for your selection.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='groups', ctx=Load()),
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
                    name='_partner_use_in',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='aggr_ids', annotation=None, type_comment=None),
                            arg(arg='models', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check if there is no occurence of this group of partner in the selected model\n            :param aggr_ids : stringified list of partner ids separated with a comma (sql array_agg)\n            :param models : dict mapping a model name with its foreign key with res_partner table\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='model', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='search_count',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='field', ctx=Load()),
                                                                Constant(value='in', kind=None),
                                                                Name(id='aggr_ids', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='model', ctx=Store()),
                                                        Name(id='field', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='models', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
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
                    name='_get_ordered_partner',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Helper : returns a `res.partner` recordset ordered by create_date/active fields\n            :param partner_ids : list of partner ids to sort\n        ', kind=None),
                        ),
                        Return(
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
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='active',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='p', ctx=Load()),
                                                                attr='create_date',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='datetime', ctx=Load()),
                                                                    attr='datetime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value=1970, kind=None),
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value=1, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='reverse',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
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
                    name='_compute_models',
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
                            value=Constant(value=' Compute the different models needed by the system if you want to exclude some partners. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model_mapping', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='exclude_contact',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='model_mapping', ctx=Load()),
                                            slice=Constant(value='res.users', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='partner_id', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='account.move.line', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='exclude_journal_item',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='model_mapping', ctx=Load()),
                                            slice=Constant(value='account.move.line', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='partner_id', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='model_mapping', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_skip',
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
                            value=Constant(value=" Skip this wizard line. Don't compute any thing, and simply redirect to the new step.", kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='current_line_id',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='current_line_id',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_action_next_screen',
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
                    name='_action_next_screen',
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
                            value=Constant(value=' return the action of the next screen ; this means the wizard is set to treat the\n            next wizard line. Each line is a subset of partner that can be merged together.\n            If no line left, the end screen will be displayed (but an action is still returned).\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='current_line', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='line_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='current_partner_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='literal_eval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='current_line', ctx=Load()),
                                                attr='aggr_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='current_line_id', kind=None),
                                                    Constant(value='partner_ids', kind=None),
                                                    Constant(value='dst_partner_id', kind=None),
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='current_line', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='current_partner_ids', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_get_ordered_partner',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='current_partner_ids', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            slice=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='selection', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='current_line_id', kind=None),
                                                    Constant(value='partner_ids', kind=None),
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='finished', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='form', kind=None),
                                    Constant(value='new', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_process_query',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='query', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Execute the select request and write the result in this wizard\n            :param query : the SQL query used to fill the wizard line\n        ', kind=None),
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
                            targets=[Name(id='model_mapping', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_models',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Name(id='query', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='counter', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='min_id', ctx=Store()),
                                    Name(id='aggr_ids', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partners', ctx=Store())],
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
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='aggr_ids', ctx=Load()),
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
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='partners', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='model_mapping', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_partner_use_in',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='partners', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='model_mapping', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base.partner.merge.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='wizard_id', kind=None),
                                                    Constant(value='min_id', kind=None),
                                                    Constant(value='aggr_ids', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='min_id', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='partners', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='counter', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='state', kind=None),
                                            Constant(value='number_group', kind=None),
                                        ],
                                        values=[
                                            Constant(value='selection', kind=None),
                                            Name(id='counter', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='counter: %s', kind=None),
                                    Name(id='counter', ctx=Load()),
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
                    name='action_start_manual_process',
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
                            value=Constant(value=" Start the process 'Merge with Manual Check'. Fill the wizard according to the group_by and exclude\n            options, and redirect to the first step (treatment of first wizard line). After, for each subset of\n            partner to merge, the wizard will be actualized.\n                - Compute the selected groups (with duplication)\n                - If the user has selected the 'exclude_xxx' fields, avoid the partners\n        ", kind=None),
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
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_selected_groupby',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_generate_query',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='groups', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='maximum_group',
                                        ctx=Load(),
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
                                    attr='_process_query',
                                    ctx=Load(),
                                ),
                                args=[Name(id='query', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_action_next_screen',
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
                    name='action_start_automatic_process',
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
                            value=Constant(value=" Start the process 'Merge Automatically'. This will fill the wizard with the same mechanism as 'Merge\n            with Manual Check', but instead of refreshing wizard with the current line, it will automatically process\n            all lines by merging partner grouped according to the checked options.\n        ", kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='action_start_manual_process',
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
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='literal_eval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='aggr_ids',
                                                ctx=Load(),
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
                                            attr='_merge',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
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
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='commit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='finished', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='form', kind=None),
                                    Constant(value='new', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='parent_migration_process_cb',
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
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value='\n            SELECT\n                min(p1.id),\n                array_agg(DISTINCT p1.id)\n            FROM\n                res_partner as p1\n            INNER join\n                res_partner as p2\n            ON\n                p1.email = p2.email AND\n                p1.name = p2.name AND\n                (p1.parent_id = p2.id OR p1.id = p2.parent_id)\n            WHERE\n                p2.id IS NOT NULL\n            GROUP BY\n                p1.email,\n                p1.name,\n                CASE WHEN p1.parent_id = p2.id THEN p2.id\n                    ELSE p1.id\n                END\n            HAVING COUNT(*) >= 2\n            ORDER BY\n                min(p1.id)\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_process_query',
                                    ctx=Load(),
                                ),
                                args=[Name(id='query', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='literal_eval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='aggr_ids',
                                                ctx=Load(),
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
                                            attr='_merge',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
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
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='commit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='finished', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n            UPDATE\n                res_partner\n            SET\n                is_company = NULL,\n                parent_id = NULL\n            WHERE\n                parent_id = id\n        ', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='form', kind=None),
                                    Constant(value='new', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_update_all_process',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='parent_migration_process_cb',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='group_by_vat', kind=None),
                                            Constant(value='group_by_email', kind=None),
                                            Constant(value='group_by_name', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
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
                                    value=Name(id='wizard', ctx=Load()),
                                    attr='action_start_automatic_process',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n            UPDATE\n                res_partner\n            SET\n                is_company = NULL\n            WHERE\n                parent_id IS NOT NULL AND\n                is_company IS NOT NULL\n        ', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_action_next_screen',
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
                    name='action_merge',
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
                            value=Constant(value=' Merge Contact button. Merge the selected partners, and redirect to\n            the end screen (since there is no other wizard line to process.\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='partner_ids',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='state', kind=None)],
                                                values=[Constant(value='finished', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='view_mode', kind=None),
                                            Constant(value='target', kind=None),
                                        ],
                                        values=[
                                            Constant(value='ir.actions.act_window', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='form', kind=None),
                                            Constant(value='new', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_merge',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner_ids',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dst_partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='current_line_id',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='current_line_id',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_action_next_screen',
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
