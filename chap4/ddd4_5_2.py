"""
4.5.2節のコードの説明
"""
from ddd4_5_1_1 import PhysicalDistributionBase

# リスト4.15
class TransportService:
    """
    輸送ドメインサービス

    Attributes: None
    """
    def transport(from_: PhysicalDistributionBase, to: PhysicalDistributionBase, baggage: Baggage):
        """
        輸送する

        Args:
            from_ (PhysicalDistributionBase): 出庫する拠点
            to (PhysicalDistributionBase): 入庫する拠点
            baggage (Baggage): 輸送する荷物
        
        Returns: None

        Note:
            ぎこちなさがなくなることを確認
        """
        shipped_baggage: Baggage = from_.ship(baggage)
        to.receive(shipped_baggage)

        # 配送の記録を行う