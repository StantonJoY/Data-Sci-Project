Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
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
        ClassDef(
            name='Followers',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' mail_followers holds the data related to the follow mechanism inside\n    Odoo. Partners can choose to follow documents (records) of any kind\n    that inherits from mail.thread. Following documents allow to receive\n    notifications for new messages. A subscription is characterized by:\n\n    :param: res_model: model of the followed objects\n    :param: res_id: ID of resource (may be 0 for every objects)\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mail.followers', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='partner_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_log_access', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Document Followers', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_model', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Related Document Model Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2oneReference',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Related Document ID', kind=None)],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Id of the followed resource', kind=None),
                            ),
                            keyword(
                                arg='model_field',
                                value=Constant(value='res_model', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_id', ctx=Store())],
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
                                value=Constant(value='Related Partner', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='type', kind=None),
                                                Constant(value='!=', kind=None),
                                                Constant(value='private', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='subtype_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mail.message.subtype', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Subtype', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Message subtypes followed, meaning subtypes that will be pushed onto the user's Wall.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='partner_id.name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Email', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='partner_id.email', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is Active', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='partner_id.active', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_invalidate_documents',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Invalidate the cache of the documents followed by ``self``.\n\n        Modifying followers change access rights to individual documents. As the\n        cache may contain accessible/inaccessible data, one has to refresh it.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='to_invalidate', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='vals_list', ctx=Load()),
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='res_model', kind=None),
                                                Constant(value='res_id', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='res_model',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='res_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='rec', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res_id', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='to_invalidate', ctx=Load()),
                                                        slice=Call(
                                                            func=Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='res_model', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='res_id', kind=None)],
                                                        keywords=[],
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
                            arg(arg='vals_list', annotation=None, type_comment=None),
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
                                            Name(id='Followers', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='_invalidate_documents',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
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
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='res_model', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='res_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_invalidate_documents',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Followers', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Name(id='x', ctx=Load()),
                                            ops=[In()],
                                            comparators=[Name(id='vals', ctx=Load())],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=List(
                                                    elts=[
                                                        Constant(value='res_model', kind=None),
                                                        Constant(value='res_id', kind=None),
                                                        Constant(value='partner_id', kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_invalidate_documents',
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
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                                    attr='_invalidate_documents',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Followers', ctx=Load()),
                                            Name(id='self', ctx=Load()),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='mail_followers_res_partner_res_model_id_uniq', kind=None),
                                    Constant(value='unique(res_model,res_id,partner_id)', kind=None),
                                    Constant(value='Error, a partner cannot follow twice the same object.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_recipient_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='message_type', annotation=None, type_comment=None),
                            arg(arg='subtype_id', annotation=None, type_comment=None),
                            arg(arg='pids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Private method allowing to fetch recipients data based on a subtype.\n        Purpose of this method is to fetch all data necessary to notify recipients\n        in a single query. It fetches data from\n\n         * followers (partners and channels) of records that follow the given\n           subtype if records and subtype are set;\n         * partners if pids is given;\n\n        :param records: fetch data from followers of records that follow subtype_id;\n        :param message_type: mail.message.message_type in order to allow custom behavior depending on it (SMS for example);\n        :param subtype_id: mail.message.subtype to check against followers;\n        :param pids: additional set of partner IDs from which to fetch recipient data;\n\n        :return: list of recipient data which is a tuple containing\n          partner ID ,\n          active value (always True for channels),\n          share status of partner,\n          notification status of partner or channel (email or inbox),\n          user groups of partner,\n        ', kind=None),
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
                                        slice=Constant(value='mail.followers', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='subtype_ids', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='mail.message.subtype', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='internal', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='active', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='active', kind=None),
                                            Constant(value='partner_share', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='res.groups', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='users', kind=None)],
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
                                    Name(id='records', ctx=Load()),
                                    Name(id='subtype_id', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Constant(value='\nSELECT DISTINCT ON (pid) * FROM (\n    WITH sub_followers AS (\n        SELECT fol.partner_id,\n               coalesce(subtype.internal, false) as internal\n          FROM mail_followers fol\n          JOIN mail_followers_mail_message_subtype_rel subrel ON subrel.mail_followers_id = fol.id\n          JOIN mail_message_subtype subtype ON subtype.id = subrel.mail_message_subtype_id\n         WHERE subrel.mail_message_subtype_id = %s\n           AND fol.res_model = %s\n           AND fol.res_id IN %s\n\n     UNION ALL\n\n        SELECT id,\n               FALSE\n          FROM res_partner\n         WHERE id=ANY(%s)\n    )\n    SELECT partner.id as pid,\n           partner.active as active,\n           partner.partner_share as pshare,\n           users.notification_type AS notif,\n           array_agg(groups_rel.gid) AS groups\n      FROM res_partner partner\n LEFT JOIN res_users users ON users.partner_id = partner.id\n                          AND users.active\n LEFT JOIN res_groups_users_rel groups_rel ON groups_rel.uid = users.id\n      JOIN sub_followers ON sub_followers.partner_id = partner.id\n                        AND NOT (sub_followers.internal AND partner.partner_share)\n        GROUP BY partner.id,\n                 users.notification_type\n) AS x\nORDER BY pid, notif\n', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Name(id='subtype_id', ctx=Load()),
                                            Attribute(
                                                value=Name(id='records', ctx=Load()),
                                                attr='_name',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='records', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='pids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='query', ctx=Load()),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='params', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='fetchall',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='pids', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='params', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='query_pid', ctx=Store())],
                                            value=Constant(value='\nSELECT partner.id as pid,\npartner.active as active, partner.partner_share as pshare,\nusers.notification_type AS notif, NULL AS groups\nFROM res_partner partner\nLEFT JOIN res_users users ON users.partner_id = partner.id AND users.active\nWHERE partner.id IN %s', kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='params', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[Name(id='pids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='query', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='SELECT DISTINCT ON (pid) * FROM (%s) AS x ORDER BY pid, notif', kind=None),
                                                op=Mod(),
                                                right=Name(id='query_pid', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='query', ctx=Load()),
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[Name(id='params', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='fetchall',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_subscription_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='doc_data', annotation=None, type_comment=None),
                            arg(arg='pids', annotation=None, type_comment=None),
                            arg(arg='include_pshare', annotation=None, type_comment=None),
                            arg(arg='include_active', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Private method allowing to fetch follower data from several documents of a given model.\n        Followers can be filtered given partner IDs and channel IDs.\n\n        :param doc_data: list of pair (res_model, res_ids) that are the documents from which we\n          want to have subscription data;\n        :param pids: optional partner to filter; if None take all, otherwise limitate to pids\n        :param include_pshare: optional join in partner to fetch their share status\n        :param include_active: optional join in partner to fetch their active flag\n\n        :return: list of followers data which is a list of tuples containing\n          follower ID,\n          document ID,\n          partner ID,\n          followed subtype IDs,\n          share status of partner (returned only if include_pshare is True)\n          active flag status of partner (returned only if include_active is True)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='where_clause', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' OR ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=List(
                                            elts=[Constant(value='fol.res_model = %s AND fol.res_id IN %s', kind=None)],
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='doc_data', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='where_params', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='itertools', ctx=Load()),
                                                attr='chain',
                                                ctx=Load(),
                                            ),
                                            attr='from_iterable',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(id='rm', ctx=Load()),
                                                        Call(
                                                            func=Name(id='tuple', ctx=Load()),
                                                            args=[Name(id='rids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='rm', ctx=Store()),
                                                                Name(id='rids', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Name(id='doc_data', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sub_where', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='pids', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='sub_where', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[Constant(value='fol.partner_id IN %s', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='where_params', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='pids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='pids', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='sub_where', ctx=Store()),
                                            op=Add(),
                                            value=List(
                                                elts=[Constant(value='fol.partner_id IS NULL', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='sub_where', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='where_clause', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='AND (%s)', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Constant(value=' OR ', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='sub_where', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='\nSELECT fol.id, fol.res_id, fol.partner_id, array_agg(subtype.id)%s%s\nFROM mail_followers fol\n%s\nLEFT JOIN mail_followers_mail_message_subtype_rel fol_rel ON fol_rel.mail_followers_id = fol.id\nLEFT JOIN mail_message_subtype subtype ON subtype.id = fol_rel.mail_message_subtype_id\nWHERE %s\nGROUP BY fol.id%s%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        IfExp(
                                            test=Name(id='include_pshare', ctx=Load()),
                                            body=Constant(value=', partner.partner_share', kind=None),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                        IfExp(
                                            test=Name(id='include_active', ctx=Load()),
                                            body=Constant(value=', partner.active', kind=None),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                        IfExp(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='include_pshare', ctx=Load()),
                                                    Name(id='include_active', ctx=Load()),
                                                ],
                                            ),
                                            body=Constant(value='LEFT JOIN res_partner partner ON partner.id = fol.partner_id', kind=None),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                        Name(id='where_clause', ctx=Load()),
                                        IfExp(
                                            test=Name(id='include_pshare', ctx=Load()),
                                            body=Constant(value=', partner.partner_share', kind=None),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                        IfExp(
                                            test=Name(id='include_active', ctx=Load()),
                                            body=Constant(value=', partner.active', kind=None),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='query', ctx=Load()),
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[Name(id='where_params', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
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
                    name='_insert_followers',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='partner_ids', annotation=None, type_comment=None),
                            arg(arg='subtypes', annotation=None, type_comment=None),
                            arg(arg='customer_ids', annotation=None, type_comment=None),
                            arg(arg='check_existing', annotation=None, type_comment=None),
                            arg(arg='existing_policy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value='skip', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Main internal method allowing to create or update followers for documents, given a\n        res_model and the document res_ids. This method does not handle access rights. This is the\n        role of the caller to ensure there is no security breach.\n\n        :param subtypes: see ``_add_followers``. If not given, default ones are computed.\n        :param customer_ids: see ``_add_default_followers``\n        :param check_existing: see ``_add_followers``;\n        :param existing_policy: see ``_add_followers``;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sudo_self', ctx=Store())],
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
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default_partner_id',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='subtypes', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='new', ctx=Store()),
                                                Name(id='upd', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_default_followers',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='res_model', ctx=Load()),
                                            Name(id='res_ids', ctx=Load()),
                                            Name(id='partner_ids', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='customer_ids',
                                                value=Name(id='customer_ids', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='check_existing',
                                                value=Name(id='check_existing', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='existing_policy',
                                                value=Name(id='existing_policy', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='new', ctx=Store()),
                                                Name(id='upd', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_followers',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='res_model', ctx=Load()),
                                            Name(id='res_ids', ctx=Load()),
                                            Name(id='partner_ids', ctx=Load()),
                                            Name(id='subtypes', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='check_existing',
                                                value=Name(id='check_existing', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='existing_policy',
                                                value=Name(id='existing_policy', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='new', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sudo_self', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Call(
                                                    func=Name(id='dict', ctx=Load()),
                                                    args=[Name(id='values', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg='res_id',
                                                            value=Name(id='res_id', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='res_id', ctx=Store()),
                                                                Name(id='values_list', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='new', ctx=Load()),
                                                                attr='items',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                    comprehension(
                                                        target=Name(id='values', ctx=Store()),
                                                        iter=Name(id='values_list', ctx=Load()),
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
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='fol_id', ctx=Store()),
                                    Name(id='values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='upd', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sudo_self', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='fol_id', ctx=Load())],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_default_followers',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='partner_ids', annotation=None, type_comment=None),
                            arg(arg='customer_ids', annotation=None, type_comment=None),
                            arg(arg='check_existing', annotation=None, type_comment=None),
                            arg(arg='existing_policy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value='skip', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Shortcut to ``_add_followers`` that computes default subtypes. Existing\n        followers are skipped as their subscription is considered as more important\n        compared to new default subscription.\n\n        :param customer_ids: optional list of partner ids that are customers. It is used if computing\n         default subtype is necessary and allow to avoid the check of partners being customers (no\n         user or share user). It is just a matter of saving queries if the info is already known;\n        :param check_existing: see ``_add_followers``;\n        :param existing_policy: see ``_add_followers``;\n\n        :return: see ``_add_followers``\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='partner_ids', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='default', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                        Name(id='external', ctx=Store()),
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
                                        slice=Constant(value='mail.message.subtype', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='default_subtypes',
                                    ctx=Load(),
                                ),
                                args=[Name(id='res_model', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='partner_ids', ctx=Load()),
                                    Compare(
                                        left=Name(id='customer_ids', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='customer_ids', ctx=Store())],
                                    value=Attribute(
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
                                                                Constant(value='id', kind=None),
                                                                Constant(value='in', kind=None),
                                                                Name(id='partner_ids', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='partner_share', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value=True, kind=None),
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
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='p_stypes', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='pid', ctx=Load()),
                                                IfExp(
                                                    test=Compare(
                                                        left=Name(id='pid', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='customer_ids', ctx=Load())],
                                                    ),
                                                    body=Attribute(
                                                        value=Name(id='external', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    orelse=Attribute(
                                                        value=Name(id='default', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='pid', ctx=Store()),
                                                iter=Name(id='partner_ids', ctx=Load()),
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_followers',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res_model', ctx=Load()),
                                    Name(id='res_ids', ctx=Load()),
                                    Name(id='partner_ids', ctx=Load()),
                                    Name(id='p_stypes', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='check_existing',
                                        value=Name(id='check_existing', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='existing_policy',
                                        value=Name(id='existing_policy', ctx=Load()),
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
                    name='_add_followers',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='partner_ids', annotation=None, type_comment=None),
                            arg(arg='subtypes', annotation=None, type_comment=None),
                            arg(arg='check_existing', annotation=None, type_comment=None),
                            arg(arg='existing_policy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value='skip', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Internal method that generates values to insert or update followers. Callers have to\n        handle the result, for example by making a valid ORM command, inserting or updating directly\n        follower records, ... This method returns two main data\n\n         * first one is a dict which keys are res_ids. Value is a list of dict of values valid for\n           creating new followers for the related res_id;\n         * second one is a dict which keys are follower ids. Value is a dict of values valid for\n           updating the related follower record;\n\n        :param subtypes: optional subtypes for new partner followers. This\n          is a dict whose keys are partner IDs and value subtype IDs for that\n          partner.\n        :param channel_subtypes: optional subtypes for new channel followers. This\n          is a dict whose keys are channel IDs and value subtype IDs for that\n          channel.\n        :param check_existing: if True, check for existing followers for given\n          documents and handle them according to existing_policy parameter.\n          Setting to False allows to save some computation if caller is sure\n          there are no conflict for followers;\n        :param existing policy: if check_existing, tells what to do with already\n          existing followers:\n\n          * skip: simply skip existing followers, do not touch them;\n          * force: update existing with given subtypes only;\n          * replace: replace existing with new subtypes (like force without old / new follower);\n          * update: gives an update dict allowing to add missing subtypes (no subtype removal);\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='_res_ids', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='res_ids', ctx=Load()),
                                    List(
                                        elts=[Constant(value=0, kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='data_fols', ctx=Store()),
                                        Name(id='doc_pids', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(id='i', ctx=Load()),
                                                        Call(
                                                            func=Name(id='set', ctx=Load()),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Name(id='_res_ids', ctx=Load()),
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
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='check_existing', ctx=Load()),
                                    Name(id='res_ids', ctx=Load()),
                                ],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='fid', ctx=Store()),
                                            Name(id='rid', ctx=Store()),
                                            Name(id='pid', ctx=Store()),
                                            Name(id='sids', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_subscription_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='res_model', ctx=Load()),
                                                            Name(id='res_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='partner_ids', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='existing_policy', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='force', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='pid', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='doc_pids', ctx=Load()),
                                                                        slice=Name(id='rid', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='add',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='pid', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='data_fols', ctx=Load()),
                                                    slice=Name(id='fid', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='rid', ctx=Load()),
                                                    Name(id='pid', ctx=Load()),
                                                    Name(id='sids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='existing_policy', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='force', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
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
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='data_fols', ctx=Load()),
                                                                    attr='keys',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='new', ctx=Store()),
                                        Name(id='update', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='res_id', ctx=Store()),
                            iter=Name(id='_res_ids', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='partner_id', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='partner_ids', ctx=Load()),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='partner_id', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='doc_pids', ctx=Load()),
                                                        slice=Name(id='res_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='new', ctx=Load()),
                                                                    attr='setdefault',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='res_id', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='list', ctx=Load()),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='res_model', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                    Constant(value='subtype_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='res_model', ctx=Load()),
                                                                    Name(id='partner_id', ctx=Load()),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='subtypes', ctx=Load()),
                                                                                        slice=Name(id='partner_id', ctx=Load()),
                                                                                        ctx=Load(),
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
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='existing_policy', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='replace', kind=None),
                                                                    Constant(value='update', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Tuple(
                                                                    elts=[
                                                                        Name(id='fol_id', ctx=Store()),
                                                                        Name(id='sids', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Tuple(
                                                                            elts=[
                                                                                Name(id='key', ctx=Load()),
                                                                                Subscript(
                                                                                    value=Name(id='val', ctx=Load()),
                                                                                    slice=Constant(value=2, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Tuple(
                                                                                    elts=[
                                                                                        Name(id='key', ctx=Store()),
                                                                                        Name(id='val', ctx=Store()),
                                                                                    ],
                                                                                    ctx=Store(),
                                                                                ),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='data_fols', ctx=Load()),
                                                                                        attr='items',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[],
                                                                                ),
                                                                                ifs=[
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Subscript(
                                                                                                    value=Name(id='val', ctx=Load()),
                                                                                                    slice=Constant(value=0, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Name(id='res_id', ctx=Load())],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Subscript(
                                                                                                    value=Name(id='val', ctx=Load()),
                                                                                                    slice=Constant(value=1, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Name(id='partner_id', ctx=Load())],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=False, kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='new_sids', ctx=Store())],
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Name(id='set', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='subtypes', ctx=Load()),
                                                                            slice=Name(id='partner_id', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                op=Sub(),
                                                                right=Call(
                                                                    func=Name(id='set', ctx=Load()),
                                                                    args=[Name(id='sids', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='old_sids', ctx=Store())],
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Name(id='set', ctx=Load()),
                                                                    args=[Name(id='sids', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                op=Sub(),
                                                                right=Call(
                                                                    func=Name(id='set', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='subtypes', ctx=Load()),
                                                                            slice=Name(id='partner_id', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='update_cmd', ctx=Store())],
                                                            value=List(elts=[], ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='fol_id', ctx=Load()),
                                                                    Name(id='new_sids', ctx=Load()),
                                                                ],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='update_cmd', ctx=Store()),
                                                                    op=Add(),
                                                                    value=ListComp(
                                                                        elt=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='Command', ctx=Load()),
                                                                                attr='link',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='sid', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='sid', ctx=Store()),
                                                                                iter=Name(id='new_sids', ctx=Load()),
                                                                                ifs=[],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='fol_id', ctx=Load()),
                                                                    Name(id='old_sids', ctx=Load()),
                                                                    Compare(
                                                                        left=Name(id='existing_policy', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='replace', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='update_cmd', ctx=Store()),
                                                                    op=Add(),
                                                                    value=ListComp(
                                                                        elt=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='Command', ctx=Load()),
                                                                                attr='unlink',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='sid', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='sid', ctx=Store()),
                                                                                iter=Name(id='old_sids', ctx=Load()),
                                                                                ifs=[],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=Name(id='update_cmd', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='update', ctx=Load()),
                                                                            slice=Name(id='fol_id', ctx=Load()),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Dict(
                                                                        keys=[Constant(value='subtype_ids', kind=None)],
                                                                        values=[Name(id='update_cmd', ctx=Load())],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='new', ctx=Load()),
                                    Name(id='update', ctx=Load()),
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
